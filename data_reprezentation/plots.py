from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


def get_data():
    data_set = pd.read_csv("../data/result/data.csv")
    x = data_set.iloc[:, :-2].values
    y = data_set.iloc[:, -2:].values

    x = x[:, 1:]
    x = x[:, :-1]
    return x, y


x, y = get_data()
plt.plot(y[:, 0], x[:, 0], 'r^', label="RSSI AP1")
plt.plot(y[:, 0], x[:, 1], 'g^', label="RSSI AP2")
plt.plot(y[:, 0], x[:, 2], 'b^', label="RSSI AP3")
plt.xlabel("x coordinate [meters]")
plt.ylabel("RSSI")
plt.legend()
plt.show()

plt.plot(y[:, 1], x[:, 0], 'r^', label="RSSI AP1")
plt.plot(y[:, 1], x[:, 1], 'g^', label="RSSI AP2")
plt.plot(y[:, 1], x[:, 2], 'b^', label="RSSI AP3")
plt.xlabel("y coordinate [meters]")
plt.ylabel("RSSI")
plt.legend()
plt.show()
