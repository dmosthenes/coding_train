import random
from PIL import Image

def get_left(grid, coords):
    return grid[coords[0]][coords[1]-1]['right']

def get_top(grid, coords):
    return grid[coords[0]-1][coords[1]]['bottom']

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
                    left_values = get_left(grid, (row, col))
                    choice = random.choice(left_values)

                elif col == 0:
                    # Check only top
                    top_values  = get_top(grid, (row, col))
                    choice = random.choice(top_values)

                else:
                    top_values  = get_top(grid, (row, col))
                    left_values = get_left(grid, (row, col))
                    values = []
                    for value in top_values:
                        if value in left_values:
                            values.append(value)
                    choice = random.choice(values)

                grid[row][col] = lookup[choice]

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

    image.save('e.png')

def main():
    grid = [[None] * 10 for i in range(10)]

    blank =  './images/blank.png'
    Tup =    './images/Tup.png'
    Tdown =  './images/Tdown.png'
    Tright = './images/Tright.png'
    Tleft =  './images/Tleft.png'
    crossroad = './images/crossroads.png'
    PVc = './images/PipeVertical.png'
    PHz = './images/PipeHorizontal.png'
    BLElbow = './images/BottomLeftElbow.png'
    BRElbow = './images/BottomRightElbow.png'
    TLElbow = './images/TopLeftElbow.png'
    TRElbow = './images/TopRightElbow.png'

    lookup = {
        'blank':     {'name': 'blank',     'image': blank,     'right': ['blank', 'Tright', 'PVc', 'BRElbow', 'TRElbow'],                    'left': ['blank',  'Tleft', 'PVc', 'BLElbow', 'TLElbow'],                                'top': ['blank', 'Tup', 'PHz', 'TLElbow', 'TRElbow'],                          'bottom': ['blank', 'Tdown', 'PHz', 'BLElbow', 'BRElbow']},
        'Tup':       {'name': 'Tup',       'image': Tup,       'right': ['Tup', 'Tdown', 'Tleft', 'crossroad', 'PHz', 'BLElbow'],            'left': ['Tup', 'Tdown', 'Tright', 'crossroad', 'PHz', 'BRElbow', 'TLElbow', 'TRElbow'], 'top': ['Tdown', 'Tright', 'Tleft', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['blank', 'Tdown', 'PHz', 'BLElbow', 'BRElbow']},
        'Tdown':     {'name': 'Tdown',     'image': Tdown,     'right': ['Tup', 'Tdown', 'Tleft', 'crossroad', 'PHz', 'BLElbow'],            'left': ['Tup', 'Tdown', 'Tright', 'crossroad', 'PHz', 'BRElbow', 'TLElbow', 'TRElbow'], 'top': ['blank', 'Tup', 'PHz', 'TLElbow', 'TRElbow'],                          'bottom': ['Tup', 'Tright', 'Tleft', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'Tright':    {'name': 'Tright',    'image': Tright,    'right': ['Tup', 'Tdown', 'Tleft', 'crossroad', 'PHz', 'BLElbow', 'TLElbow'], 'left': ['blank', 'Tleft', 'PVc', 'BLElbow', 'TLElbow'],                                 'top': ['Tdown', 'Tright', 'Tleft', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['Tup', 'Tright', 'Tleft', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'Tleft':     {'name': 'Tleft',     'image': Tleft,     'right': ['blank', 'Tright', 'PVc', 'BRElbow', 'TRElbow'],                    'left': ['Tup', 'Tdown', 'Tright', 'crossroad', 'PHz', 'BRElbow', 'TRElbow'],            'top': ['Tdown', 'Tright', 'Tleft', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['Tup', 'Tright', 'Tleft', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'BLElbow':   {'name': 'BLElbow',   'image': BLElbow,   'right': ['blank', 'Tright', 'PVc', 'BRElbow', 'TRElbow'],                    'left': ['Tdown', 'Tright', 'Tup', 'crossroad', 'PHz', 'BRElbow', 'TRElbow'],            'top': ['blank', 'Tup', 'PHz', 'TLElbow', 'TRElbow'],                          'bottom': ['Tleft', 'Tright', 'Tup', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'BRElbow':   {'name': 'BRElbow',   'image': BRElbow,   'right': ['Tdown', 'Tleft', 'Tup', 'crossroad', 'PHz', 'BLElbow', 'TLElbow'], 'left': ['blank', 'Tleft', 'PVc', 'BLElbow', 'TLElbow'],                                 'top': ['blank', 'Tup', 'PHz', 'TLElbow', 'TRElbow'],                          'bottom': ['Tleft', 'Tright', 'Tup', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'TLElbow':   {'name': 'TLElbow',   'image': TLElbow,   'right': ['blank', 'Tright', 'PVc', 'BRElbow', 'TRElbow'],                    'left': ['Tdown', 'Tright', 'Tup', 'crossroad', 'PHz', 'BRElbow', 'TRElbow'],            'top': ['Tdown', 'Tleft', 'Tright', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['blank', 'Tdown', 'PHz', 'BLElbow', 'BRElbow']},
        'TRElbow':   {'name': 'TRElbow',   'image': TRElbow,   'right': ['Tdown', 'Tleft', 'Tup', 'crossroad', 'PHz', 'BLElbow', 'TLElbow'], 'left': ['blank', 'Tleft', 'PVc', 'BLElbow', 'TLElbow'],                                 'top': ['Tdown', 'Tleft', 'Tright', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['blank', 'Tdown', 'PHz', 'BLElbow', 'BRElbow']},
        'crossroad': {'name': 'crossroad', 'image': crossroad, 'right': ['Tdown', 'Tleft', 'Tup', 'crossroad', 'PHz', 'BLElbow', 'TLElbow'], 'left': ['Tdown', 'Tright', 'Tup', 'crossroad', 'PHz', 'BRElbow', 'TRElbow'],            'top': ['Tdown', 'Tleft', 'Tright', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['Tleft', 'Tright', 'Tup', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']},
        'PHz':       {'name': 'PHz',       'image': PHz,       'right': ['Tdown', 'Tleft', 'Tup', 'crossroad', 'PHz', 'BLElbow', 'TLElbow'], 'left': ['Tdown', 'Tright', 'Tup', 'crossroad', 'PHz', 'TRElbow'],                       'top': ['blank', 'Tup', 'PHz', 'TLElbow', 'TRElbow'],                          'bottom': ['blank', 'Tdown', 'PHz', 'BLElbow']},
        'PVc':       {'name': 'PVc',       'image': PVc,       'right': ['blank', 'Tright', 'PVc', 'BRElbow', 'TRElbow'],                    'left': ['blank', 'Tleft', 'PVc', 'BLElbow', 'TLElbow'],                                 'top': ['Tdown', 'Tleft', 'Tright', 'crossroad', 'PVc', 'BLElbow', 'BRElbow'], 'bottom': ['Tleft', 'Tright', 'Tup', 'crossroad', 'PVc', 'TLElbow', 'TRElbow']}
    }

    fill_grid(grid, lookup)
    make_image(grid)

if __name__ == '__main__':
    main()