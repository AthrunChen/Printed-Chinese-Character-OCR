from keras.models import load_model
import dataencode
from keras.optimizers import SGD
import numpy as np
from keras.callbacks import ModelCheckpoint

parameter = dataencode.encode()
X_train = parameter['arr_0']
y_train = parameter['arr_1']
# index = np.arange(84617)
# np.random.shuffle(index)
# X_train = X_test[index, :, :, :]
# y_train = y_test[index, :]
print(X_train.shape)
print(y_train.shape)


sgd = SGD(lr=0.00002, decay=1e-7, momentum=0.9, nesterov=True)
model = load_model('MK4.hdf5')
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])

checkpointer = ModelCheckpoint(filepath='MK4.hdf5', verbose=1, save_best_only=True)
model.fit(X_train, y_train, epochs=40, batch_size=32, verbose=1, validation_split=0.03, callbacks=[checkpointer])
model.save('MK4.h5')



# loss, accurate = model.evaluate(x=x_test, y=y_train)
# print('loss', loss)
# print('accurate', accurate)

