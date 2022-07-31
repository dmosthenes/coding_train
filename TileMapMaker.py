import random
from constants import *
from PIL import Image

class CreateTileMap():
    def __init__(self):
        self.size = 5
        self.tilesets = tilesets

    def get_left(self, coords):
        return self.grid[coords[0]][coords[1]-1]['polarity'][1]

    def get_top(self, coords):
        return self.grid[coords[0]-1][coords[1]]['polarity'][2]

    def grab_blocks(self, lookup, west=None, north=None):
        
        blocks = []
        for i in lookup.keys():
            if (lookup[i]['polarity'][0] == north or north == None) and (lookup[i]['polarity'][3] == west or west == None):
                blocks.append(lookup[i])
        
        return blocks

    def create_grid(self, size):
        '''
        size = The n By n dimensions of your image multiplied by the pixels of the image being used
        '''
        self.size = size
        self.grid = [[None] * size for i in range(size)]
        return self.grid

    def fill_grid(self, lookup):
        '''
        lookup = a dictionary containing information about the images, found in constants.py
        '''
        while True:
            break_loop = False
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):

                    # sets first value at random
                    if row == 0 and col == 0:
                        keys = list(lookup.keys())
                        self.grid[0][0] = lookup[random.choice(keys)]

                    else:
                        if row == 0:
                            # Check only Left
                            left_value = self.get_left((row, col))
                            possible_blocks = self.grab_blocks(lookup, west=left_value)

                        elif col == 0:
                            # Check only top
                            top_value  = self.get_top((row, col))
                            possible_blocks = self.grab_blocks(lookup, north=top_value)

                        else:
                            top_value  = self.get_top((row, col))
                            left_value = self.get_left((row, col))
                            possible_blocks = self.grab_blocks(lookup, west=left_value, north=top_value)

                        if len(possible_blocks) == 0:
                            break_loop = True
                        else:
                            choice = random.choice(possible_blocks)
                            self.grid[row][col] = choice
                    
                    if break_loop: break
                if break_loop: break
            if break_loop:
                self.create_grid(self.size)
            else:
                break

    def make_image(self, file_name, step):
        '''
        file_name = (str) Whatever name you want to give the file.
        
        step = Usually the width in pixels of each image being used. Ex. 16
        '''
        height = step*len(self.grid)
        width = step*len(self.grid)
        image = Image.new(mode='RGB', size=(height, width), color=255)

        # Draw images
        y = 0
        for row in self.grid:
            x = 0
            for temp in row:
                im = Image.open(temp['image'])
                im = im.rotate(angle=90*temp['rotation'])
                im = im.resize((step, step))
                image.paste(im, box=(x*step, y*step))
                x += 1
            y += 1
            
        image.save(f'{file_name}.png')