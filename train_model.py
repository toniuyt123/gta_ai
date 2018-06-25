from alexnet import alexnet
import numpy as np
import argparse

WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 8
NAME = 'gtasa-drive-{}-{}-video.model'.format(LR, EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

save_path = 'data/polished1-4.npy'

def main():
    train_data = np.load(save_path)
    train = train_data[:-250]
    test = train_data[-250:]
    print(train[0][0])
    print(train[0][1])

    train_x = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
    train_y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
    test_y = [i[1] for i in test]

    model.fit({'input': train_x}, {'targets': train_y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=500, show_metric=True, run_id=NAME)

    model.save(NAME)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test model')
    parser.add_argument('-w', '--width', metavar='Width')
    parser.add_argument('--ht', '--heigth', metavar='Height')
    parser.add_argument('--lr', metavar='Learning rate')
    parser.add_argument('-e', '--epochs', metavar='Epochs')
    parser.add_argument('--save', '--save_path', metavar='Save path')
    args = parser.parse_args()

    WIDTH = int(args.width) if args.width is not None else WIDTH 
    HEIGHT = int(args.ht) if args.ht is not None else HEIGHT
    LR = float(args.lr) if args.lr is not None else LR
    EPOCHS = int(args.epochs) if args.epochs is not None else EPOCHS
    save_path = args.save if args.save is not None else save_path
    NAME = 'gtasa-drive-{}-{}-kek.model'.format(LR, EPOCHS)
    main()