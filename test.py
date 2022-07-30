lookup = {
        # name  :     N  E  S  W
        'Tright':    {'image': 'Tright',    'polarity': [1, 1, 1, 0]},
        'TRElbow':   {'image': 'TRElbow',   'polarity': [1, 1, 0, 0]},
        'PVc':       {'image': 'PVc',       'polarity': [1, 0, 1, 0]}
    }

west = 0
north = 1

blocks = []
for i in lookup.keys():
    if lookup[i]['polarity'][0] == north and lookup[i]['polarity'][3] == west:
        blocks.append(lookup[i])
