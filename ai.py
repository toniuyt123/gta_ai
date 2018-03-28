import imgProcessing as ip
import keyboardPress as kp

def drive(screen):
    lanes = ip.detect_lanes(screen)
    try:
        leftLine = lanes[0]
        rightLine = lanes[1]

        slopeLeft = ip.calc_slope(leftLine[0][0], leftLine[0][1], leftLine[0][2], leftLine[0][3])
        slopeRight = ip.calc_slope(rightLine[0][0], rightLine[0][1], rightLine[0][2], rightLine[0][3])
        print(slopeLeft)
        print(slopeRight)
        
        if slopeLeft < 0 and slopeRight < 0:
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