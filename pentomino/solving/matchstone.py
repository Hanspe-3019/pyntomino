'''
Ermittelt die Lagen eines Steins, die nur freie Positionen belegen

next solver                   :       1       2.2 s               2.1 s   97%
    get_good_posis            :   59714      14.2 s   238.5 µs   14.3 s  100%
    get_good_posis_old        :   59714      11.1 s   185.3 µs   11.1 s  100%
    check_holes               :   27394       2.5 s    91.7 µs    2.5 s  100%
'''
import numpy as np
from pentomino.solving import perfproxy as perftree

@perftree.time_it
def get_good_posis(pos, space):
    '''Alle Lagen eines Steins auf pos = .positions + (x,y,z),
        - die in den Space passen und
        - auf freien Feldern liegen.
        - Der Rand des Space ist reserviert, also Koordinaten > 0 und < shape-1
    '''
    # pos.shape=(n,5,3), n=Anzahl der Lagen, 5 Positionen der Würfel, [x,y,z]
    max_pos = np.array(space.shape) - 1
    in_space = np.all(
        (pos > 0) & (pos < max_pos),
        axis=(1,2)
        )  # mask : in_space.shape ist (n, )

    pos_in_space = pos[in_space].reshape((-1, 5, 3))
    if len(pos_in_space) == 0:
        return []

    wheres = np.moveaxis(pos_in_space, 1, 2)   # shape=(n,3,5)

    check_free = [
        np.all( space[tuple(xyz)] == 0) for xyz in wheres
    ]

    result = wheres[check_free]

    return result

def setup_test():
    ''' der klassische 5*4*3-Quader
    mit F in der Ecke vorne unten links
    '''
    # pylint: disable=import-outside-toplevel
    from pentomino import pento
    space = np.zeros((7,6,5), dtype=np.int8)
    space.fill(-1)
    space[1:6, 1:5, 1:4] = 0
    space[1:6, 1:5, 1:4] = 0

    lagen = pento.get_pentominos()['F'].positions
    return (lagen + (1,1,1), space)

@perftree.time_it
def get_good_posis_old(pos, space):
    '''Alle Lagen eines Steins auf pos = .positions + (x,y,z),
        - die in den Space passen und
        - auf freien Feldern liegen.
        - Der Rand des Space ist reserviert, also Koordinaten > 0 und < shape-1
    '''
    # pos.shape=(n,5,3), n=Anzahl der Lagen, 5 Positionen der Würfel, [x,y,z]
    max_pos = np.array(space.shape) - 1
    in_space = np.all(
        (pos > 0) & (pos < max_pos),
        axis=(1,2)
        )  # mask : in_space.shape ist (n, )
    # pos[in_space].shape=(y,5,3)
    # p.T shape=(3,5)
    # p.T.tolist() [0] x, [1] y, [2] z - Koordinate des Würfels
    posis = [p.T.tolist() for p in pos[in_space]]

    if len(posis) == 0:
        return []

    # Jetzt noch der Test, ob alles frei ist:
    testzero = np.array([space[tuple(p)] for p in posis])

    # .nonzero() returns tuple of np.array, one for each dim
    passt = np.all(testzero == 0, axis=1).nonzero()[0]

    return np.array(posis)[passt]
