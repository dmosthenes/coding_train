import random
from PIL import Image, ImageDraw

def find_best_entropy(grid, lookup):
    best_entropy_coords = None
    best_entropy_dict   = {}
    for i in grid:
        pass
    
    return (0, 0), 'e'

def make_image(grid):
    step = 16
    height = step*len(grid)
    width = step*len(grid)
    image = Image.new(mode='L', size=(height, width), color=255)


    # Draw images
    y = 0
    for row in grid:
        x = 0
        for temp in row:
            im = Image.open(temp['image'])
            image.paste(im, box=(y*step, x*step))
            x += 1
        y += 1

    image.save('e.png')

def main():
    grid = [
        [[], [], []],
        [[], [], []],
        [[], [], []]
    ]

    blank =  './images/blank.png'
    Tup =    './images/Tup.png'
    Tdown =  './images/Tdown.png'
    Tright = './images/Tright.png'
    Tleft =  './images/Tleft.png'

    lookup = {
        'blank':  {'name': 'blank', 'image': blank,  'right': [blank, Tright],     'left': [blank, Tleft],       'top': [blank, Tup],           'bottom': [blank, Tdown]},
        'Tup':    {'name': 'Tup', 'image': Tup,    'right': [Tup, Tdown, Tleft], 'left': [Tup, Tdown, Tright], 'top': [Tdown, Tright, Tleft], 'bottom': [blank, Tdown]},
        'Tdown':  {'name': 'Tdown', 'image': Tdown,  'right': [Tup, Tdown, Tleft], 'left': [Tup, Tdown, Tright], 'top': [blank, Tup],           'bottom': [Tup, Tright, Tleft]},
        'Tright': {'name': 'Tright', 'image': Tright, 'right': [Tup, Tdown, Tleft], 'left': [blank, Tleft],       'top': [Tdown, Tright, Tleft], 'bottom': [Tup, Tright, Tleft]},
        'Tleft':  {'name': 'Tleft', 'image': Tleft,  'right': [blank, Tright],     'left': [Tup, Tdown, Tright], 'top': [Tdown, Tright, Tleft], 'bottom': [Tup, Tright, Tleft]}
    }

    # Sets first index to random image
    keys = list(lookup.keys())
    for row in grid:
        for num in range(len(row)):
            row[num] = lookup[random.choice(keys)]

    while True:
        double_break = True
        for row in grid:
            if [] in row: 
                double_break = False
                break
        
        if double_break: break

        coords, image_dict = find_best_entropy(grid, lookup)


    make_image(grid)

if __name__ == '__main__':
    main()