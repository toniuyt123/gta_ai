import imgProcessing as ip
import keyboardPress as kp
import math

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

