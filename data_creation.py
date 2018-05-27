import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
import msvcrt
import win32api as wapi
import argparse

stopped = True
save_path = 'training_data.npy'

key_list = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    key_list.append(char)

def key_check():
    keys = []
    for key in key_list:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def key_to_output(keys) :
    output = [0,0,0,0]
    global stopped
    if 'A' in keys:
        output[0] = 1
    if 'D' in keys:
        output[3] = 1
    if 'W' in keys:
        output[1] = 1
    if 'S' in keys:
        output[2] = 1

    if 'P' in keys:
        stopped = not stopped
        print('Stopped' if stopped else 'Resumed')
        time.sleep(1)

    return output
def create_file(save_path):
    training_data = []
    if os.path.isfile(save_path):
        print('File already exists')
        training_data = list(np.load(save_path))
    else:
        print('Creating new file')
    return training_data

def main(save_path):
    training_data = create_file(save_path)
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
            training_data.append([screen, key])
            if len(training_data) % 1000 == 0:
                print(len(training_data))
                np.save(save_path,training_data)

            lap = time.time() - prevTime
            #print(lap)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows() 
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create the actual data')
    parser.add_argument('--save', '--save-path', '--sp', metavar='Save path')
    args = parser.parse_args()
    save_path = args.save if args.save is not None else save_path
    main(save_path)
