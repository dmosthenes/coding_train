import random

class Point:

    def __init__(self, width, height):
        self.x = random.random()
        self.y = random.random()

        self.label = 1 if self.x >= self.y else -1

    def get_inputs(self):
        return (self.x, self.y)
    
    def get_label(self):
        return self.label

    


