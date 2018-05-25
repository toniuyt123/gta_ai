import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
import msvcrt
import win32api as wapi

stopped = True
fileName = 'training_short3.npy'

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def key_to_output(keys) :
    output = [0,0,0]#,0]
    global stopped
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    elif 'W' in keys:
        output[1] = 1
    '''if 'S' in keys:
        output[2] = 1'''

    if 'P' in keys:
        stopped = not stopped
        print('Stopped' if stopped else 'Resumed')
        time.sleep(1)

    return output
def create_file(fileName):
    trainingData = []
    if os.path.isfile(fileName):
        print('File already exists')
        trainingData = list(np.load(fileName))
    else:
        print('Creating new file')
    return trainingData

def main(fileName):
    trainingData = create_file(fileName)
    time.sleep(5)
    print('Stopped press p to resume')
    while(True): 
        key = key_to_output(key_check())
        if not stopped:
            prevTime = time.time()
            screen =  np.array(ImageGrab.grab(bbox=(50,50,800,650)))
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            screen = cv2.resize(screen, (120, 90))
            #cv2.imshow('window',screen)
            print(key)
            trainingData.append([screen, key])
            if len(trainingData) % 1000 == 0:
                print(len(trainingData))
                np.save(fileName,trainingData)

            lap = time.time() - prevTime
            #print(lap)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows() 
                break

main(fileName)