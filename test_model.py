from data_creation import key_check
import cv2
import numpy as np
from PIL import ImageGrab
import time
import keyboardPress as kp
from alexnet import alexnet

stopped = True
WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 8
NAME = 'gtasa-drive-{}-{}.model'.format(LR, EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)
model.load(NAME)
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
                kp.Forward()
            elif prediction[0] > sides_threshold:
                kp.TurnLeftF()
            elif prediction[2] > sides_threshold:
                kp.TurnRightF()

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
main()