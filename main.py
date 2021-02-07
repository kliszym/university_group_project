from numpy import mean
from numpy import std
from numpy import asarray
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.model_selection import RepeatedKFold


def get_model(n_inputs, n_outputs):
    model = Sequential()
    model.add(Dense(20, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
    model.add(Dense(n_outputs))
    model.compile(loss='mae', optimizer='adam', metrics='mean_absolute_error')
    return model


def get_data(data_file_path):
    data_set = pd.read_csv(data_file_path)
    x = data_set.iloc[:, :-2].values
    y = data_set.iloc[:, -2:].values

    x = x[:, 1:]
    x = x[:, :-1]

    x = np.asarray(x).astype('float32')
    y = np.asarray(y).astype('float32')

    return x, y


train_data_file_path = "data/result/data.csv"
validation_data_file_path = "data/result/validation.csv"
tests_data_file_path = "data/result_tests/data.csv"

x_train, y_train = get_data(train_data_file_path)
x_val, y_val = get_data(validation_data_file_path)
x_tests, y_tests = get_data(tests_data_file_path)

n_inputs, n_outputs = x_train.shape[1], y_train.shape[1]
model = get_model(n_inputs, n_outputs)
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), verbose=1, epochs=500)

yhat = model.predict(x_tests)

error = []
for predicted_data in zip(yhat, y_tests):
    error.append(sqrt(((predicted_data[0][0] - predicted_data[1][0]) * (predicted_data[0][0] - predicted_data[1][0])) +
                 ((predicted_data[0][1] - predicted_data[1][1]) * (predicted_data[0][1] - predicted_data[1][1]))))

plt.plot(history.history['mean_absolute_error'][10:])
plt.plot(history.history['val_mean_absolute_error'][10:])
plt.xlabel("epoch")
plt.ylabel("error [m]")
plt.legend(["MEA", "validation MEA"])
plt.show()

plt.plot(error)
plt.xlabel("test data index")
plt.ylabel("error [m]")
plt.show()

print('MAE: %s' % str((sum(error) / len(error))))
