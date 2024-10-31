from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

import matplotlib.pyplot as plt

import pandas as pd


data = pd.read_csv('cancer.csv')
X = data.iloc[: , :-1].values
y = data.iloc[: , -1].values

# Scale the data to [0, 1]
scaler   = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# Initialize the Self-Organizing Map
som = MiniSom(x=10, y=10, input_len=X.shape[1])
# Randomly initialize the weights
som.random_weights_init(X_scaled)
# Train the SOM
som.train_random(X_scaled, num_iteration=100)


# Visualize the results
plt.figure(figsize=(10, 10))
for i, x in enumerate(X_scaled):
    win = som.winner(x)  # Get the winning node
    x_val = win[0] + 0.5
    y_val = win[1] + 0.5
    plt.text(x_val, y_val, str(y[i]), color=plt.cm.rainbow(y[i]/2))

plt.axis([0, som_x, 0, som_y])
plt.gca().invert_yaxis()
plt.show()