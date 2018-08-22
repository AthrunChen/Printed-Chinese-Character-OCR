import mymodel
from keras.datasets import mnist
from keras.utils import np_utils
from keras import optimizers
import numpy as np
import dataencode
from keras.optimizers import SGD
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import keras


class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


nb_classes = 3500
parameter = dataencode.encode(path='D:\\datasetplus10', class_num=nb_classes, proportion=0, data_num=nb_classes*60)
# X = np.load("x_train.npz")
# Y = np.load("y_train.npz")

X_train = parameter['x_train']
y_train = parameter['y_train']

print(X_train.shape)
print(y_train.shape)
print("data loaded")

#X_train = X_train.reshape(len(X_train), -1)
#X_test = X_test.reshape(len(X_test), -1)

X_train = X_train.astype('float32')
X_train = (X_train - 127) / 127
#X_test = (X_test - 127) / 127
#X_train = np.expand_dims(X_train, axis=4)

print(X_train.shape)


#y_train = np_utils.to_categorical(y_train, nb_classes)
#y_test = np_utils.to_categorical(y_test, nb_classes)

sgd = SGD(lr=0.0015, decay=1e-7, momentum=0.9, nesterov=True)
# model = load_model('MK11.h5')
model = mymodel.athmodel(nb_classes=nb_classes)
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
# checkpointer = ModelCheckpoint(filepath='temp.h5', verbose=1, save_best_only=True)
history = LossHistory()
model.fit(X_train, y_train, epochs=10, batch_size=64, verbose=1, validation_split=0.2, callbacks=[history])
print(history.losses)
model.save("temp.h5")





