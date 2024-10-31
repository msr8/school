from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np


data = pd.read_csv('cancer.csv')
X = data.iloc[: , :-1].values
y = data.iloc[: , -1].values


# Scale the data to [0, 1]
scaler   = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Initialize the Self-Organizing Map
som = MiniSom(x=10, y=10, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)
som.train(data=X_scaled, num_iteration=100)

# Visualize the results
plt.figure(figsize=(10, 10))
for i, x in enumerate(X_scaled):
    w = som.winner(x)  # Get the winning node
    plt.text(w[0]+0.5, w[1]+0.5, str(y[i]), color=plt.cm.rainbow(y[i] / 2), fontdict={'weight': 'bold', 'size': 11})

plt.axis([0, som_x, 0, som_y])
# plt.gca().invert_yaxis()
plt.show()
