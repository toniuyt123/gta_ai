import cv2
import numpy as np
from PIL import ImageGrab
import time

def detect_lanes(screen):
    grey = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 60, 110)
    roi = [(0, 0), (0, 350), (300, 250), (500, 250), (800, 350), (800, 0)]
    cv2.fillPoly(edges, [np.array(roi)], 0)
    lines = cv2.HoughLinesP(edges,rho=1,theta=np.pi/180,threshold=10, minLineLength=120, maxLineGap=15)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                cv2.line(edges,(x1,y1),(x2,y2),(0,255,0),5)
    except TypeError:
        print("TypeError...")

    return edges

while(True): 
    prevTime = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,600)))
    screen = detect_lanes(screen)
    cv2.imshow('window',screen)
    
    lap = time.time() - prevTime
    print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

