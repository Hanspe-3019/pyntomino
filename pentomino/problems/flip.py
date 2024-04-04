''' Flip eines Raums über eine der drei Ebenen
'''
import numpy as np

#      Ebene  y-z         x-z         x-y
AXES = {'x': (1,2), 'y': (0,2), 'z': (0,1)}

def flip_by(raum, by):
    ''' Die Rotationsebene wird mit x, y oder z angegeben
    '''
    return np.rot90(raum, k=2, axes=AXES[by])
