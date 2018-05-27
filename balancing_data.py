import numpy as np
import random
import cv2
import argparse

file_path = 'data/training_short_balanced1+2.npy'
save_file_path = 'data/training_short_balanced1+2no_zeroes.npy'
train_data = [None]
result = [None]

counters = [None]

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
    return shortest

def balance_data(file_path, train_data):
    counters = [0] * len(train_data[0][1])
    shortest = process_counters(counters, train_data)
    counters = [0] * len(train_data[0][1])
    #forwards = 0
    #counters[1] /= 2
    '''for data in train_data:
        image = data[0]
        choice = data[1]
        if choice == [0,1,0,0] and forwards < counters[1]:
            result.append([image, choice])
            forwards += 1
        elif choice != [0,1,0,0]:
            result.append([image, choice])'''
    for data in train_data:
        image = data[0]
        choice = data[1]
        indexes = get_indexes(choice, 1)
        for index in indexes:
            if counters[index] < shortest:
                #print(counters[index])
                counters[index] += 1
                result.append([image, choice])

    random.shuffle(result)

    np.save(file_path, result)

def main():
    '''train_data = np.load(file_path)
    random.shuffle(train_data)
    remove_empty(train_data)
    balance_data(save_file_path, train_data)'''
    concat_data("dawey.npy" ,"./data/training_short_balanced4.npy")

def print_screen(screen):
    screen = cv2.resize(screen, (800, 600))
    cv2.imshow('image', screen)
    #print(train_data[0][1])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def concat_data(file_path, second_file_path):
    train_data = np.load(file_path)
    train_data2 = np.load(second_file_path)
    result = []
    for data in train_data:
        result.append([data[0], data[1]])
    for data in train_data2:
        try:
            result.append([data[0], data[1]])
        except TypeError:
            print("damn")

    random.shuffle(result)
    np.save(save_file_path, result)

def remove_empty(train_data):
    result = []
    for data in train_data:
        if data[1] != [0, 0, 0]:
            result.append(data)

    np.save(save_file_path, result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Balance data used for training the model')
    parser.add_argument('--save', '--save-path', '--sp', metavar='Save path')
    parser.add_argument('--file', '--file-path', '--fp', metavar='File path')
    args = parser.parse_args()
    file_path = args.file if args.file is not None else file_path
    save_file_path = args.save if args.save is not None else save_file_path
    main()
