# import libraries
import numpy
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
from keras.models import load_model
import matplotlib.pyplot as plt
# K.set_image_data_format('channels_first')

# Load cidfar dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Store train and test data
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0

# Use to_categorical function from np_utils for making it into categorical value
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# QUESTION1
# sequential model
model = Sequential()

# Convolutional input layer, 32 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), padding='same', activation='relu', kernel_constraint=maxnorm(3)))

# Dropout layer at 20%.
model.add(Dropout(0.2))

# Convolutional layer, 32 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))

# Max Pool layer with size 2×2.
model.add(MaxPooling2D(pool_size=(2, 2)))

# Convolutional layer, 64 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(64, (3, 3), padding='same', activation='relu', kernel_constraint=maxnorm(3)))

 # Dropout layer at 20%.
model.add(Dropout(0.2))

# Convolutional layer, 64 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))

# Max Pool layer with size 2×2.
model.add(MaxPooling2D(pool_size=(2, 2)))

#Convolutional layer, 128 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(128, (3, 3), padding='same', activation='relu', kernel_constraint=maxnorm(3)))

# Dropout layer at 20%.
model.add(Dropout(0.2))

# Convolutional layer,128 feature maps with a size of 3×3 and a rectifier activation function.
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))

#  Max Pool layer with size 2×2.
model.add(MaxPooling2D(pool_size=(2, 2)))

#  Flatten layer.
model.add(Flatten())

# Dropout layer at 20%.
model.add(Dropout(0.2))

# Fully connected layer with 1024 units and a rectifier activation function.
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))

# Dropout layer at 20%.
model.add(Dropout(0.2))

# Fully connected layer with 512 units and a rectifier activation function.
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))

# Dropout layer at 20%.
model.add(Dropout(0.2))

# Fully connected output layer with 10 units and a softmax activation function
model.add(Dense(num_classes, activation='softmax'))

# Compile model
epochs = 6
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
print(model.summary())
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=128)
# save the model
model.save('cifar10.h5')
# Final evaluation of the model
model = load_model('cifar10.h5')
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

