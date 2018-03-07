import cv2
import numpy as np
from PIL import ImageGrab
import time

while(True): 
    screen =  np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break