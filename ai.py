import imgProcessing as ip
import keyboardPress as kp
import math
import car_detection as cd
import cv2

def drive(screen):
    lanes = ip.detect_lanes(screen)
    try:
        left_line = lanes[0]
        right_line = lanes[1]

        slope_left = ip.calc_slope(left_line[0][0], left_line[0][1], left_line[0][2], left_line[0][3])
        slope_right = ip.calc_slope(right_line[0][0], right_line[0][1], right_line[0][2], right_line[0][3])
        print(slope_left)
        print(slope_right)
        
        if slope_left == 0:
            print("crossroad")
            kp.turn_left()
        elif slope_left < 0 and slope_right < 0:
            print("turn right")
            kp.turn_right_f()
        elif slope_left > 0 and slope_right > 0:
            print("turn left")
            kp.turn_left_f()
        else:
            print("forward")
            kp.forward()
    except TypeError:
        return None

def drive2(screen):
    lines = ip.get_lines(screen)
    weight = 0

    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = ip.calc_slope(x1, y1, x2, y2)
                angle_weight = math.cos(angle)
                if(angle_weight < 0):
                    weight -= 1
                elif(angle_weight > 0):
                    weight += 1

        print(weight)

        if(abs(weight) < round(len(lines)*0.6)):
            kp.forward()
        elif(weight > 0):
            kp.turn_left_f()
        elif(weight < 0):
            kp.turn_right_r()
    except TypeError:
        print("no lines man")

def drive3(screen, model, WIDTH, HEIGHT, fw_threshold=50, left_threshold=50, right_threshold=50):
    car_bboxes = cd.get_object(screen)
    collision_warning = False
    for car_bbox in car_bboxes:
        if length_of_bounding_box(car_bbox, WIDTH) >= (WIDTH * 0.35):
            mid_point_x = mid_point(car_bbox)[0]
            if mid_point_x > 0.33 and mid_point_x < 0.66:
                screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
                screen = cv2.resize(screen, (WIDTH, HEIGHT))
                prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
                print(prediction)
                collision_warning = True
                '''if prediction[1] > fw_threshold:
                    kp.forward()
                elif prediction[0] > left_threshold:
                    kp.turn_left_f()
                elif prediction[2] > right_threshold:
                    kp.turn_right_f()'''

                print("yolo")
                break
            
    if not collision_warning:
        print("not yolo")
        #drive2(screen)
        

def length_of_bounding_box(bbox, WIDTH):
    return bbox[3]*WIDTH - bbox[1]*WIDTH

def mid_point(bbox):
    return [(bbox[3] + bbox[1]) / 2, (bbox[2] + bbox[0]) / 2]