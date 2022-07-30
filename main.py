import random
from PIL import Image

def get_left(grid, coords):
    return grid[coords[0]][coords[1]-1]['polarity'][1]

def get_top(grid, coords):
    return grid[coords[0]-1][coords[1]]['polarity'][2]

def grab_blocks(lookup, west=None, north=None):
    
    blocks = []
    for i in lookup.keys():
        if (lookup[i]['polarity'][0] == north or north == None) and (lookup[i]['polarity'][3] == west or west == None):
            blocks.append(lookup[i])
    
    return blocks

def fill_grid(grid, lookup):
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # sets first value at random
            if row == 0 and col == 0:
                keys = list(lookup.keys())
                grid[0][0] = lookup[random.choice(keys)]

            else:
                if row == 0:
                    # Check only Left
                    left_value = get_left(grid, (row, col))
                    possible_blocks = grab_blocks(lookup, west=left_value)

                elif col == 0:
                    # Check only top
                    top_value  = get_top(grid, (row, col))
                    possible_blocks = grab_blocks(lookup, north=top_value)

                else:
                    top_value  = get_top(grid, (row, col))
                    left_value = get_left(grid, (row, col))
                    possible_blocks = grab_blocks(lookup, west=left_value, north=top_value)

                choice = random.choice(possible_blocks)
                grid[row][col] = choice

def make_image(grid):
    step = 16
    height = step*len(grid)
    width = step*len(grid)
    image = Image.new(mode='RGB', size=(height, width), color=255)

    # Draw images
    y = 0
    for row in grid:
        x = 0
        for temp in row:
            im = Image.open(temp['image'])
            image.paste(im, box=(x*step, y*step))
            x += 1
        y += 1
        
    image.save('test.png')

def main(size):
    grid = [[None] * size for i in range(size)]

    blank =       './images/blank.png'
    Tup =         './images/Tup.png'
    Tdown =       './images/Tdown.png'
    Tright =      './images/Tright.png'
    Tleft =       './images/Tleft.png'
    crossroad =   './images/crossroads.png'
    PVc =         './images/PipeVertical.png'
    PHz =         './images/PipeHorizontal.png'
    BLElbow =     './images/BottomLeftElbow.png'
    BRElbow =     './images/BottomRightElbow.png'
    TLElbow =     './images/TopLeftElbow.png'
    TRElbow =     './images/TopRightElbow.png'
    D1 =          './images/deadend1.png'
    D2 =          './images/deadend2.png'
    D3 =          './images/deadend3.png'
    D4 =          './images/deadend4.png'
    fd =          './images/forkdown.png'
    fu =          './images/forkup.png'
    fl =          './images/forkleft.png'
    fr =          './images/forkright.png'
    fed1 =        './images/forkenddown.png'
    fed2 =        './images/forkenddown2.png'
    feu1 =        './images/forkendup.png'
    feu2 =        './images/forkendup2.png'
    fer1 =        './images/forkendright.png'
    fer2 =        './images/forkendright2.png'
    fel1 =        './images/forkendleft.png'
    fel2 =        './images/forkendleft2.png'
    spiderdown =  './images/spiderdown.png'
    spiderup =    './images/spiderup.png'
    spiderleft =  './images/spiderleft.png'
    spiderright = './images/spiderright.png'
    fishdown =    './images/fishdown.png'
    fishup =      './images/fishup.png'
    fishleft =    './images/fishleft.png'
    fishright =   './images/fishright.png'

    # Blank  = 0
    # Normal = 1
    lookup = {
        # name  :  N  E  S  W
        'blank' :      {'image': blank,       'polarity': [0, 0, 0, 0]},
        'Tup':         {'image': Tup,         'polarity': [1, 1, 0, 1]},
        'Tdown':       {'image': Tdown,       'polarity': [0, 1, 1, 1]},
        'Tright':      {'image': Tright,      'polarity': [1, 1, 1, 0]},
        'Tleft':       {'image': Tleft,       'polarity': [1, 0, 1, 1]},
        'BLElbow':     {'image': BLElbow,     'polarity': [0, 0, 1, 1]},
        'BRElbow':     {'image': BRElbow,     'polarity': [0, 1, 1, 0]},
        'TLElbow':     {'image': TLElbow,     'polarity': [1, 0, 0, 1]},
        'TRElbow':     {'image': TRElbow,     'polarity': [1, 1, 0, 0]},
        'crossroad':   {'image': crossroad,   'polarity': [1, 1, 1, 1]},
        'PHz':         {'image': PHz,         'polarity': [0, 1, 0, 1]},
        'PVc':         {'image': PVc,         'polarity': [1, 0, 1, 0]},
        'D1':          {'image': D1,          'polarity': [1, 0, 0, 1]},
        'D2':          {'image': D2,          'polarity': [0, 0, 0, 1]},
        'D3':          {'image': D3,          'polarity': [1, 1, 1, 1]},
        'D4':          {'image': D4,          'polarity': [1, 1, 1, 1]},
        'fd':          {'image': fd,          'polarity': [1, 0, 2, 0]},
        'fu':          {'image': fu,          'polarity': [2, 0, 1, 0]},
        'fl':          {'image': fl,          'polarity': [0, 1, 0, 2]},
        'fr':          {'image': fr,          'polarity': [0, 2, 0, 1]},
        'fed1':        {'image': fed1,        'polarity': [0, 0, 2, 0]},
        'fed2':        {'image': fed2,        'polarity': [0, 0, 2, 0]},
        'feu1':        {'image': feu1,        'polarity': [2, 0, 0, 0]},
        'feu2':        {'image': feu2,        'polarity': [2, 0, 0, 0]},
        'fer1':        {'image': fer1,        'polarity': [0, 2, 0, 0]},
        'fer2':        {'image': fer2,        'polarity': [0, 2, 0, 0]},
        'fel1':        {'image': fel1,        'polarity': [0, 0, 0, 2]},
        'fel2':        {'image': fel2,        'polarity': [0, 0, 0, 2]},
        'spiderdown':  {'image': spiderdown,  'polarity': [1, 2, 2, 2]},
        'spiderup':    {'image': spiderup,    'polarity': [2, 2, 1, 2]},
        'spiderleft':  {'image': spiderleft,  'polarity': [2, 1, 2, 2]},
        'spiderright': {'image': spiderright, 'polarity': [2, 2, 2, 1]},
        'fishdown':    {'image': fishdown,    'polarity': [1, 1, 2, 1]},
        'fishup':      {'image': fishup,      'polarity': [2, 1, 1, 1]},
        'fishleft':    {'image': fishleft,    'polarity': [1, 1, 1, 2]},
        'fishright':   {'image': fishright,   'polarity': [1, 2, 1, 1]}
    }

    fill_grid(grid, lookup)
    make_image(grid)

if __name__ == '__main__':
    size = 150
    main(size)