''' Flip eines Raums über eine der drei Ebenen
'''
import numpy as np

#       Ebene  y-z         x-z         x-y
_AXES = {'x': (1,2), 'y': (0,2), 'z': (0,1)}

def flip_it(space, plane):
    ''' Die Rotationsebene wird mit x, y oder z angegeben
    '''
    return rotate_it(space, plane, by=2)

def rotate_it(space, plane, by=1):
    ' - '
    return np.rot90(space, k=by, axes=_AXES[plane])
