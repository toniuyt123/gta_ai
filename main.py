import cv2
import numpy as np
from PIL import ImageGrab
import time
import ai

time.sleep(5)
while(True): 
    prev_time = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
    #ai.drive2(screen)
    
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    #cv2.imshow('window',screen)

    lap = time.time() - prev_time
    print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break