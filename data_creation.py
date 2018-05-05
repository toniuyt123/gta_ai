import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
import msvcrt

def key_to_output(key) :
    output = [0,0,0]
    
    if 'a' == key:
        output[0] = 1
    elif 'd' == key:
        output[2] = 1
    else:
        output[1] = 1

    return output


fileName = 'training_data.npy'

if os.path.isfile(fileName):
    print('File already exists')
    trainingData = list(np.load(fileName))
else:
    print('Creating new file')
    trainingData = []

time.sleep(5)
while(True): 
    prevTime = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    screen = cv2.resize(screen, (80, 60))
    #cv2.imshow('window',screen)

    key = 0
    if msvcrt.kbhit():
        key = msvcrt.getch()
        #print(key)
    trainingData.append([screen, key_to_output(key)])
    
    if len(trainingData) % 1000 == 0:
        print(len(trainingData))
        np.save(fileName,trainingData)

    lap = time.time() - prevTime
    #print(lap)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break