import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate linearly separable points
np.random.seed(0)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)

# Perceptron class
class Perceptron:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.weights = np.zeros(3)  # 2 weights + bias term

    def predict(self, X):
        return np.where(np.dot(X, self.weights[1:]) + self.weights[0] > 0, 1, -1)

    def train(self, X, y):
        errors = []
        for _ in range(10):  # Number of training iterations
            error = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                error += int(update != 0.0)
            errors.append(error)
        return errors

# Initialize perceptron
perceptron = Perceptron()

# Animation update function
def update(frame):
    if frame < len(X):
        point = X[frame]
        target = y[frame]
        perceptron.train([point], [target])
        ax.cla()

        # Calculate classifications and set colors accordingly
        predictions = perceptron.predict(X)
        colors = ['green' if prediction == target else 'red' for prediction, target in zip(predictions, y)]

        ax.scatter(X[:, 0], X[:, 1], c=colors)  # Use calculated colors
        ax.set_title(f'Frame {frame+1}')
        ax.set_xlim([-3, 3])
        ax.set_ylim([-3, 3])
        x_vals = np.array([-3, 3])
        y_vals = -(perceptron.weights[0] + perceptron.weights[1] * x_vals) / perceptron.weights[2]
        ax.plot(x_vals, y_vals, 'g--')
        ax.plot(point[0], point[1], 'ro' if target == 1 else 'bo')  # Highlight current point
        
# Create animation
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(X)+10, interval=500, repeat=False)

# Show the animation
plt.show()