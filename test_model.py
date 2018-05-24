from data_creation import key_check
import cv2
import numpy as np
from PIL import ImageGrab
import time
import keyboardPress as kp
import sys
#from alexnet import alexnet
import argparse

stopped = True
WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 8
NAME = 'gtasa-drive-{}-{}.model'.format(LR, EPOCHS)
#model = alexnet(WIDTH, HEIGHT, LR)
#model.load(NAME)
fw_threshold = 0.52
sides_threshold = 0.52

def main():
    global stopped
    print("OH BOY")
    while(True): 
        if 'P' in key_check():
            stopped = not stopped
            print('Stopped' if stopped else 'Resumed')
            kp.FullStop()
            time.sleep(1)
        if not stopped:
            screen = np.array(ImageGrab.grab(bbox=(50,50,800,650)))
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            #cv2.imshow('window',screen)
            screen = cv2.resize(screen, (WIDTH, HEIGHT))
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
            print(prediction)
            
            if prediction[1] > fw_threshold:
                kp.forward()
            elif prediction[0] > sides_threshold:
                kp.turn_left_f()
            elif prediction[2] > sides_threshold:
                kp.turn_right_f()

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test model')
    parser.add_argument('-w', '--width', metavar='Width')
    parser.add_argument('--ht', '--heigth', metavar='Height')
    parser.add_argument('--lr', metavar='Learning rate')
    parser.add_argument('-e', '--epochs', metavar='Epochs')
    parser.add_argument('--fw', '--fw-th', metavar='Forward threshold, should be between 1 and 0')
    parser.add_argument('-s', '--s-th', metavar='Sides threshold, should be between 1 and 0')
    args = parser.parse_args()

    WIDTH = int(args.width) if args.width is not None else WIDTH 
    HEIGHT = int(args.ht) if args.ht is not None else HEIGHT
    LR = float(args.lr) if args.lr is not None else LR
    EPOCHS = int(args.epochs) if args.epochs is not None else EPOCHS
    fw_threshold = float(args.fw) if args.fw is not None else fw_threshold
    sides_threshold = float(args.s_th) if args.s_th is not None else sides_threshold
    NAME = 'gtasa-drive-{}-{}.model'.format(LR, EPOCHS)
    main()