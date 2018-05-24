import numpy as np
from balancing_data import get_indexes
import argparse
file_path = 'data/training_hot_data.npy'
save_path_one_hot = 'data/training_hot_data.npy'
save_path_short = 'data/training_short.npy'
train_data = []

def convert_to_one_hot(file_path, train_data):
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
    
    np.save(save_path_one_hot, result)

def shorten_data(file_path, train_data):
    result = []
    for data in train_data:
        image = data[0]
        choice = data[1]
        if choice[4] == 1:
            result_choice = [1, 0, 0]
        elif choice[5] == 1:
            result_choice = [0, 0, 1]
        else:
            #                       A          W          D 
            result_choice = [choice[0], choice[1], choice[3]]            
        result.append([image, result_choice])
    
    np.save(file_path, result)  

def main():
    #convert_to_one_hot(save_name, train_data)
    shorten_data(save_path_short, train_data)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert data used by the machine learner')
    parser.add_argument('--save-hot', '--save-path-hot', '--sph', metavar='Save path for hot array')
    parser.add_argument('--save-short', '--save-path-short', '--sps', metavar='Save path for short array')
    parser.add_argument('--file', '--file-path', '--fp', metavar='File path')
    args = parser.parse_args()
    file_path = args.file if args.file is not None else file_path
    save_path_one_hot = args.save_hot if args.save_hot is not None else save_path_one_hot
    save_path_short = args.save_short if args.save_short is not None else save_path_short
    main()