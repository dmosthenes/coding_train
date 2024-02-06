import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
import numpy as np

class Perceptron_Visualiser:

    def __init__(self, perceptron, width, height):
        self.perceptron = perceptron
        self.width = width
        self.height = height
        self.scatter_map = {}
    
    def draw_line(self):
        """
        Draw the line to the graph.
        """

        # Get the weights and bias
        weights = self.perceptron.weights
        bias = self.perceptron.bias

        # Create the line
        x = np.linspace(0, self.width, 100)
        y = -1 * (weights[0] * x + bias) / weights[1]

        if hasattr(self, 'line'):
            self.line.set_data(x,y)
        else:
            self.line, = plt.plot(x, y, '-r')

    def draw_point(self, point):
        """
        Draw the point to the graph.
        """

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        x, y = point.get_inputs()
        self.scatter_map[point] = plt.scatter(x, y, c='r' if point.label == 1 else 'b')

        plt.pause(0.001)


    def update_point_colour(self):
        """
        Update the colour of the points.
        """

        if self.scatter_map:

            # Loop over each element of the scatter map
            for point, scatter in self.scatter_map.items():

                # Predict accuracy against current line
                prediction = self.perceptron.predict(point.get_inputs())

                # Set colour according to accuracy of prediction
                scatter.set_color('g' if prediction == point.label else 'r')

                plt.draw() 


        # if self.scatter is not None:
            
        #     predictions = [self.perceptron.predict(point.get_inputs()) for point in self.points]

        #     colours = ['g' if prediction == point.get_label() else 'r' for prediction, point in zip(predictions, self.points)]

        #     self.scatter.set_color(colours)
        #     plt.draw()
                
    def title(self):
        plt.title("Gradient Descent Motherfuckers")

    def result(self, outcome):
        plt.text(0.5, -0.1, outcome, fontsize=12, ha="center", va="top")

    def reset(self):
        plt.clf()
        self.scatter_map = None

    def draw(self):
        plt.show()







