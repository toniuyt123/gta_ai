import numpy as np
import random
import cv2

file_name = 'data/training_data.npy'
train_data = np.load(file_name)
random.shuffle(train_data)
result = []

counters = []

def get_indexes(val_list, key):
    return [i for i, j in enumerate(val_list) if j == key]

def process_counters(counters, train_data):
    for data in train_data:
        choice = data[1]
        #print_screen(data[0])

        indexes = get_indexes(choice, 1)
        for index in indexes:
            counters[index] += 1

    print(counters)
    shortest = min(counters)
    #counters = [0] * len(counters)
    return counters

def balance_data(file_name, train_data):
    global counters
    counters = [0] * len(train_data[0][1])
    counters = process_counters(counters, train_data)
    forwards = 0
    counters[1] /= 2
    for data in train_data:
        image = data[0]
        choice = data[1]
        if choice == [0,1,0,0] and forwards < counters[1]:
            result.append([image, choice])
            forwards += 1
        elif choice != [0,1,0,0]:
            result.append([image, choice])
    '''for data in train_data:
        image = data[0]
        choice = data[1]

        indexes = get_indexes(choice, 1)
        for index in indexes:
            if counters[index] < shortest:
                counters[index] += 1
                result.append([image, choice])'''

    random.shuffle(result)

    np.save(file_name, result)

def main():
    balance_data(file_name, train_data)

def print_screen(screen):
    screen = cv2.resize(screen, (800, 600))
    cv2.imshow('image', screen)
    #print(train_data[0][1])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

#main()