import cv2
import numpy as np
from PIL import ImageGrab
import time
import ai
#from alexnet import alexnet

WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 8
NAME = './models/gtasa-drive-{}-{}-100k2.model'.format(LR, EPOCHS)
#model = alexnet(WIDTH, HEIGHT, LR)
#model.load(NAME)

time.sleep(1)
while(True): 
    prev_time = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
    ai.drive(screen)
    # ai.drive2(screen)
    # ai.drive3(screen, model, WIDTH, HEIGHT)

    #lap = time.time() - prev_time
    #print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break