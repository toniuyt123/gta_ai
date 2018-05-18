import numpy as np
import random
import cv2

train_data = np.load('training_data.npy')
random.shuffle(train_data)
result = []

counters = [0, 0, 0]

for data in train_data:
    choice = data[1]
    #print_screen(data[0])

    if choice == [1, 0, 0]:
        counters[0] += 1
    elif choice == [0, 1, 0]:
        counters[1] += 1
    elif choice == [0, 0, 1]:
        counters[2] += 1


print(counters)
shortest = min(counters[0], counters[1], counters[2])
counters = [0, 0, 0]

for data in train_data:
    image = data[0]
    choice = data[1]

    if choice == [1, 0, 0] and counters[0] < shortest:
        counters[0] += 1
        result.append([image, choice])
    elif choice == [0, 1, 0] and counters[1] < shortest:
        counters[1] += 1
        result.append([image, choice])
    elif choice == [0, 0, 1] and counters[2] < shortest:
        counters[2] += 1
        result.append([image, choice])

random.shuffle(result)

np.save("training_data.npy", result)

def prin_screen(screen):
    screen = cv2.resize(screen, (800, 600))
    cv2.imshow('image', screen)
    #print(train_data[0][1])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break