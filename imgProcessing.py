import cv2
import numpy as np

def get_lines(screen):
    grey = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 70, 70)
    roi = [(0, 0), (0, 400), (300, 300), (500, 300), (800, 400), (800, 0)]
    cv2.fillPoly(edges, [np.array(roi)], 0)
    lines = cv2.HoughLinesP(edges,rho=1,theta=np.pi/180,threshold=10, minLineLength=250, maxLineGap=20)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    try:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
                if(abs(angle) > 20):
                    cv2.line(edges,(x1,y1),(x2,y2),(0,255,0),5)
    except TypeError:
        i = 0

    cv2.imshow('lines',edges)

    return lines

def detect_lanes(screen):
    lines = get_lines(screen)
    try:
        lane1 = lines[0]

        cv2.line(screen,(lane1[0][0],lane1[0][1]),(lane1[0][2],lane1[0][3]),(0,255,0),5)
        for line in lines:    
            for x1,y1,x2,y2 in line:
                angle = calc_slope(x1, y1, x2, y2)
                if(abs(angle) > 20 and abs(x1 - lane1[0][0]) > 10):
                    cv2.line(screen,(x1,y1),(x2,y2),(0,255,0),5)
                    return [lines[0], line]
    except TypeError:
        return [[[100, 300, 200, 0]], [[500, 0, 700, 300]]]

def calc_slope(x1, y1, x2, y2):
    return np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
