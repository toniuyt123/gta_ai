import cv2
import numpy as np
from PIL import ImageGrab
import time
from keyboardPress import PressKey,ReleaseKey, W, A, S, D

def get_lines(screen):
    grey = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 90, 90)
    roi = [(0, 0), (0, 400), (300, 300), (500, 300), (800, 400), (800, 0)]
    cv2.fillPoly(edges, [np.array(roi)], 0)
    #cv2.fillPoly(screen, [np.array(roi)], 0)
    lines = cv2.HoughLinesP(edges,rho=1,theta=np.pi/180,threshold=10, minLineLength=250, maxLineGap=20)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
                if(abs(angle) > 20):
                    cv2.line(edges,(x1,y1),(x2,y2),(0,255,0),5)
    except TypeError:
        print("TypeError...")

    cv2.imshow('lines',edges)

    return lines

def detect_lanes(screen):
    i = 0
    lines = get_lines(screen)
    lane1 = lane2 = 0
    try:
        lane1 = lines[0]

        cv2.line(screen,(lane1[0][0],lane1[0][1]),(lane1[0][2],lane1[0][3]),(0,255,0),5)
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
                if(abs(angle) > 20 and abs(x1 - lane1[0][0]) > 10):
                    lane2 = line
                    cv2.line(screen,(x1,y1),(x2,y2),(0,255,0),5)
                    return None
    except TypeError:
        print("TypeError...")

    return lane1, lane2

def determine_action(leftLine, rightLine):
    noLeftLine = noRightLine = False
    if leftLine[0][0] <= 400 and leftLine[0][2] <= 400
        and rightLine[0][0] <= 400 and rightLine[0][2] <= 400:
        noRightLine = True
    if leftLine[0][0] >= 400 and leftLine[0][2] >= 400
        and rightLine[0][0] >= 400 and rightLine[0][2] >= 400:
        noLeftLine = True
    if noLeftLine and noRightLine or 
        not noLeftLine and not noRightLine:
        kp.Forward()
    elif not noLeftLine and noRightLine:
        kp.TurnRight()
    elif noLeftLine and not noRightLine:
        kp.TurnLeft()

while(True): 
    prevTime = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
    detect_lanes(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    cv2.imshow('window',screen)
    
    lap = time.time() - prevTime
    print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break