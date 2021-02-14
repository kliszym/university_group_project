from keras.callbacks import Callback
from math import sqrt
import matplotlib.pyplot as plt


class TestCallback(Callback):
    def __init__(self, test_data):
        self.test_data = test_data
        self.history = {"mea": []}

    def on_epoch_end(self, epoch, logs={}):
        x, y = self.test_data
        result = self.model.predict(x)

        error = []
        for predicted_data in zip(result, y):
            error.append((
                abs(predicted_data[0][0] - predicted_data[1][0]) +
                abs(predicted_data[0][1] - predicted_data[1][1]) +
                abs(predicted_data[0][2] - predicted_data[1][2]))/3)

        mea = sum(error)/len(error)
        self.history["mea"].append(mea)
        print('\nTesting MEA: {}\n'.format(mea))

    def __del__(self):
        plt.plot(self.history['mea'][10:])
        plt.xlabel("epoch")
        plt.ylabel("MAE [m]")
        plt.show()

