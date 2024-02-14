import pygame
import random

class bird():

    def __init__(self, screen):
        self.radius = 10
        self.gravity = 1
        self.x = 50
        self.y = 50
        self.yvelocity = 0
        self.colour = (255, 255, 255)
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y))
    
    def jump(self):
        self.yvelocity += 10

    def update(self):
        # update y position
        self.y += self.yvelocity

        # update velocity
        if self.yvelocity < 10:
            self.yvelocity -= self.gravity

    def check_collision(self, pipe):
        # Check if bird in within pipe's area

        # Check x position is overlapping
        if self.x > pipe.toplft[0] and self.x < pipe.toplft[0] + self.width:

            # Check y position is above or below pipe gap
            if self.y < pipe.gapy and self.y > pipe.gapy + pipe.gapdst:

                return True
            
        return False

class pipe():

    def __init__(self, screen):
        self.screen = screen
        self.width = 30
        self.height = self.screen.height
        self.toplft = (self.screen.width - self.width, 0)
        self.xvelocity = -10
        self.colour = (255, 255, 255)

        # gapy is the the y coordinate for start of gap
        self.gapy = random.randint(0, self.screen.height)
        # gapdst is the height of the gap
        self.gapdst = 50

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, 
                         (self.toplft[0], 0, 
                          self.width, self.height - self.gapy))
        pygame.draw.rect(self.screen, self.colour,
                         (self.toplft[0], self.gapdst + self.gapy,
                          self.width, self.height - self.gapy + self.gapdst))

    def update(self):
        # update toplft coordinates
        self.toplft = (self.toplft[0] + self.xvelocity, 0)
        
