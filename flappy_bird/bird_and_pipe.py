import pygame
import random
# import tensorflow as tf
# import torch
import numpy as np
import sys

from npnn import NeuralNetwork

class Bird():

    def __init__(self, screen):
        self.radius = 10
        self.gravity = 1
        self.x = 50
        self.y = 50
        self.yvelocity = 0
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.screen = screen
        self.brain = Brain()
        self.score = 0

    def __hash__(self):
        return hash(self.colour)
    
    def __eq__(self, other):
        if isinstance(other, Bird):
            return self.colour == other.colour

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.radius)
    
    def choice(self, pipe_dst, gap_top, gap_bot):
        if np.argmax(self.brain.predict(self.y, self.yvelocity, pipe_dst, gap_top, gap_bot)) == 0:
            self.jump()

    def jump(self):
        if not self.yvelocity < 0:
            self.yvelocity -= 15

    def update(self):
        # update y position
        self.y += self.yvelocity

        # update velocity
        if self.yvelocity < 10:
            self.yvelocity += self.gravity

    def collides(self, pipe):
        # Check if bird is within pipe's area
        # Check x position is overlapping
        if self.x > pipe.toplft[0] and self.x < pipe.toplft[0] + pipe.width:
            # Check y position is above or below pipe gap
            if self.y < pipe.gapy or self.y > pipe.gapy + pipe.gapdst:
                return True
        return False
    
    def out_of_bounds(self):
        if self.y < 0 or self.y > self.screen.get_height():
            return True
        return False
    
    def set_score(self, score):
        self.score = score


class Pipe():

    def __init__(self, screen):
        self.screen = screen
        self.width = 60
        self.height = self.screen.get_height()
        self.toplft = (self.screen.get_width(), 0)
        self.xvelocity = -10
        self.colour = (255, 255, 255)

        # gapy is the the y coordinate for start of gap
        self.gapy = random.randint(self.height * 0.1, self.height * 0.6)
        # gapdst is the height of the gap
        self.gapdst = 100

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, 
                         (self.toplft[0], 0, 
                          self.width, self.gapy))
        pygame.draw.rect(self.screen, self.colour,
                         (self.toplft[0], self.gapdst + self.gapy,
                          self.width, self.height - self.gapy - self.gapdst))

    def update(self):
        # update toplft coordinates
        self.toplft = (self.toplft[0] + self.xvelocity, 0)
        

class Brain():

    def __init__(self):
        self.model = NeuralNetwork(5, 4, 2)
    
    def predict(self, y_pos, y_vel, pipe_dst, gap_top, gap_bot):

        # input_data = np.array([y_pos, y_vel, pipe_dst, gap_top, gap_bot])

        input_data = [y_pos, y_vel, pipe_dst, gap_top, gap_bot]

        # input_data = input_data.reshape(-1,5)

        prediction = self.model.feedforward(input_data)
        return prediction