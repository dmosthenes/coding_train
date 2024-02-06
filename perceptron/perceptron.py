import random

def sign(n):
    return -1 if n < 0 else 1

class Perceptron():

    def __init__(self, n=2):
        self.weights = [random.randint(-1,1) for x in range(n)]
        self.bias = random.randint(-1,1)
        self.learning_rate = 0.1

    def update_weights(self, index, value):
        self.weights[index] += value

    def update_bias(self, value):
        self.bias += value
    
    def predict(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i] * inputs[i]
        sum += self.bias
        return sign(sum)

    def train(self, inputs, target):
        guess = self.predict(inputs)
        error = target - guess

        for i in range(len(self.weights)):
            self.update_weights(i, self.learning_rate * error * inputs[i])
        self.update_bias(self.learning_rate * error)

        return True if error == 0 else False

    def print_formula(self):
        print(f"y = {self.weights[0]}x + {self.weights[1]}x + {self.bias}")    

