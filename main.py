import cv2
import numpy as np
from PIL import ImageGrab
import time
import ai
#from alexnet import alexnet
from data_creation import key_check

'''WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 8
NAME = './models/gtasa-drive-{}-{}-100k2.model'.format(LR, EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)
model.load(NAME)'''
stopped = True

time.sleep(1)
while(True): 
    if 'P' in key_check():
        stopped = not stopped
        print('Stopped' if stopped else 'Resumed')
        time.sleep(1)
    if not stopped:
        prev_time = time.time()
        screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
        ai.drive(screen)
        
        #screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        #cv2.imshow('window',screen)

        lap = time.time() - prev_time
        #print(lap)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows() 
            break