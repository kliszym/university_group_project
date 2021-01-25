from numpy import mean
from numpy import std
from numpy import asarray
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import RepeatedKFold


def get_model(n_inputs, n_outputs):
    model = Sequential()
    model.add(Dense(5, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
    model.add(Dense(n_outputs))
    model.compile(loss='mae', optimizer='adam')
    return model


def get_data():
    data_set = pd.read_csv("data/result/data.csv")
    x = data_set.iloc[:, :-2].values
    y = data_set.iloc[:, -2:].values

    x = x[:, 1:]
    x = x[:, :-1]
    return x, y


x, y = get_data()
n_inputs, n_outputs = x.shape[1], y.shape[1]
model = get_model(n_inputs, n_outputs)
model.fit(np.asarray(x).astype('float32'), np.asarray(y).astype('float32'), verbose=0, epochs=100)
row = [-65.5, -68.5, -75.0]
newX = asarray([row])
yhat = model.predict(newX)

print('Predicted: %s' % yhat[0])