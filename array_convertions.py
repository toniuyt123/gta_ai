import numpy as np
from balancing_data import get_indexes
file_name = 'data/raw_training_data.npy'
save_name_one_hot = 'data/training_hot_data.npy'
save_name_short = 'data/training_short.npy'
train_data = np.load(file_name)

def convert_to_one_hot(file_name, train_data):
    result = []
    for data in train_data:
        image = data[0]
        choice = data[1]
        indexes = get_indexes(choice, 1)
        if  len(indexes) > 2:
            continue
        #                A  W  S  D WA WD SA SD 
        result_choice = [0, 0, 0, 0, 0, 0, 0, 0]
        if len(indexes) == 2:
            if indexes[0] == 0 and indexes[1] == 1:
                result_choice[4] = 1
            elif indexes[0] == 1 and indexes[1] == 3:
                result_choice[5] = 1
            elif indexes[0] == 0 and indexes[1] == 2:
                result_choice[6] = 1
            elif indexes[0] == 2 and indexes[1] == 3:
                result_choice[7] = 1
        elif len(indexes) == 1:
            result_choice[indexes[0]] = 1
            
        result.append([image, result_choice])
    
    np.save(file_name, result)

def shorten_data(file_name, train_data):
    result = []
    for data in train_data:
        image = data[0]
        choice = data[1]
        indexes = get_indexes(choice, 1)
        if  len(indexes) >= 2:
            continue
        #                A  W  D 
        result_choice = [0, 0, 0]
        if len(indexes) == 1:
            result_choice[indexes[0]] = 1
            
        result.append([image, result_choice])
    
    np.save(file_name, result)  

def main():
    #convert_to_one_hot(save_name, train_data)
    shorten_data(save_name_short, train_data)

main()