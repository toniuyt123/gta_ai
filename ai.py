import imgProcessing as ip
import keyboardPress as kp
import math

def drive(screen):
    lanes = ip.detect_lanes(screen)
    try:
        leftLine = lanes[0]
        rightLine = lanes[1]

        slopeLeft = ip.calc_slope(leftLine[0][0], leftLine[0][1], leftLine[0][2], leftLine[0][3])
        slopeRight = ip.calc_slope(rightLine[0][0], rightLine[0][1], rightLine[0][2], rightLine[0][3])
        print(slopeLeft)
        print(slopeRight)
        
        if slopeLeft == 0:
            print("crossroad")
            kp.TurnLeft()
        elif slopeLeft < 0 and slopeRight < 0:
            print("turn right")
            kp.TurnRightF()
        elif slopeLeft > 0 and slopeRight > 0:
            print("turn left")
            kp.TurnLeftF()
        else:
            print("forward")
            kp.Forward()
    except TypeError:
        return None

def drive2(screen):
    lines = ip.get_lines(screen)
    weight = 0

    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = ip.calc_slope(x1, y1, x2, y2)
                angleWeight = math.cos(angle)
                if(angleWeight < 0):
                    weight -= 1
                elif(angleWeight > 0):
                    weight += 1

        print(weight)

        if(abs(weight) < round(len(lines)*0.6)):
            kp.Forward()
        elif(weight > 0):
            kp.TurnLeftF()
        elif(weight < 0):
            kp.TurnRightF()
    except TypeError:
        print("no lines man")
    
