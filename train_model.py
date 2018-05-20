from alexnet import alexnet
import numpy as np

WIDTH = 120
HEIGHT = 90
LR = 1e-3
EPOCHS = 5
NAME = 'gtasa-drive-{}-{}.model'.format(LR, EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('data/training_hot_data.npy')

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