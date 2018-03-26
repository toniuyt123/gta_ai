import cv2
import numpy as np
from PIL import ImageGrab
import time
from keyboardPress import PressKey,ReleaseKey, W, A, S, D

def detect_lanes(screen):
    grey = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 50, 50)
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
        print("TypeError...")''' & abs(x1 - lane1[0][0]) > 40 & abs(y1 - lane1[0][2]) > 40'''

    return edges


while(True): 
    prevTime = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
    screen = detect_lanes(screen)
    cv2.imshow('window',screen)
    
    lap = time.time() - prevTime
    print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break


        '''maxY = 650
    minY = 300
    leftUpX = [None] * 100
    rightUpX = [None] * 100 
    leftDownX = [None] * 100 
    rightDownX = [None] * 100 
    lIndex = rIndex = 0

    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
                if(abs(angle) > 20):
                    if(x1 > 400 & x2 > 400):
                        if(y1 > 475):
                            rightDownX[rIndex] = x1
                            rightUpX[rIndex] = x2
                        else:
                            rightDownX[rIndex] = x2
                            rightUpX[rIndex] = x1
                        rIndex += 1
                    else:
                        if(y1 > 475):
                            leftDownX[lIndex] = x1
                            leftUpX[lIndex] = x2
                        else:
                            leftDownX[lIndex] = x2
                            leftUpX[lIndex] = x1
                        lIndex += 1
    except TypeError:
        print("TypeError...")

    lu = ld = ru = rd = 0
    try:
        ruAvr = rdAvr = luAvr = ldAvr = 0
        for i in range(0, rIndex):
            ruAvr += rightUpX[i]
            rdAvr += rightDownX[i]

        rd = rdAvr / rIndex
        ru = ruAvr / rIndex

        for i in range(0, lIndex):
            luAvr += leftUpX[i]
            ldAvr += leftDownX[i]

        ld = ldAvr / lIndex
        lu = luAvr / lIndex
    except ZeroDivisionError:
         print("NoLines...")'''