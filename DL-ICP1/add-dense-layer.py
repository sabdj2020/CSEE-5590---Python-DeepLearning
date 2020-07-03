# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

data = pd.read_csv("data/diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(data[:,0:8], data[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model

# add relu dense layer
my_first_nn.add(Dense(40, input_dim=8, activation='relu'))
my_first_nn.add(Dense(40, input_dim=40, activation='relu'))
my_first_nn.add(Dense(40, input_dim=8, activation='relu'))

my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
