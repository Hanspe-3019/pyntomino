'''Version of get_smallest_hole() using skimage.morphology
                                       count      elaps       /call      cpu   busy
    check_holes                   :   27256       2.5 s    93.2 µs    2.6 s  100%
    get_good_posis                :   57909      15.2 s   262.4 µs   15.2 s  100%

                                       count      elaps       /call      cpu   busy
    check_holes                   :    5508     502.6 ms    91.3 µs  502.8 ms  100%
        find_jammed_positions     :    2545    2111.9 ms   829.8 µs 2111.3 ms  100%
    get_good_posis                :    9202    2371.7 ms   257.7 µs 2374.1 ms  100%
'''
import numpy as np

from skimage import morphology
from pentomino.solving.perfproxy import time_it

MARK_EMPTY = 0
MARK_BACKGROUND = -1

@time_it
def check_holes(space):
    '''Checks the holes (sets connected empty places)  in <space> and
        returns tuple with size of hole and position of
     - any hole with size%5 != 0 or
     - smallest hole with size%5 == 0
     returns None, None if no holes in <space>
    '''
    my_space = space.copy()

    # Alles außer den leeren Feldern wird Background:
    my_space[np.where(space != MARK_EMPTY)] = MARK_BACKGROUND

    # label() ermittelt die Inseln gleichen Wertes und labelt sie von
    # 0 (Background) bis n = Anzahl Inseln
    # labeled hat den selben Shape wie my_space, nur der Inhalt ist hier
    # nicht der Wert von my_space (-1 oder 0), sondern die Nummer der Insel
    # in der sich die Position befindet:
    #
    # Bespiel mit background -1:
    #
    # | -1  0  0 |          | 0  1  1 |
    # | 0  -1  0 |   ===>   | 2  0  1 |
    # | 0  0  -1 |          | 2  2  0 |
    #
    labeled = morphology.label(
        my_space,
        connectivity=1,
        background=MARK_BACKGROUND,
        return_num=False
    )

    labels, sizes = np.unique(labeled, return_counts=True)
    if len(labels) == 1:
        # Ein einziges Loch, also alles belegt (außer BACKGROUND)
        return None, None
    try:
        krumm = next(size for size in sizes[1:] if size % 5 > 0)
    except StopIteration:
        pass # Alle Löcher sind Vielfache von 5
    else:
        return krumm, None    # Mindestens ein "krummes" Loch
    # Label mit kleinstem Loch:
    size_min = min(sizes[1:])  # ohne Background
    label_min = next(
        label for label, size in zip(
            labels[1:], sizes[1:] # ohne Background
        ) if size==size_min)
    pos = np.array(
            np.where(
                labeled == label_min
            )
        ).T[0]

    return (size_min, pos)

@time_it
def find_jammed_positions(): # (labeled_space, size=3):
    ''' Looking for positions with minimal count of unoccupied neighbors 
    from scipy.ndimage import generic_filter

    temp = np.empty_like(labeled_space)
    most_restricted = size ** 3
    positions_most_restricted = None

    for label in np.unique(labeled_space)[1:]: # ohne 0, BACKGROUND
        temp.fill(0)
        temp[np.where(labeled_space == label)] = 1
        neighbors_unoccupied = generic_filter(
            temp,
            np.sum,
            size=size,
            mode='constant',
            cval=0,           # 0 ist default
        )
        # Innerhalb `label` mit den wenigsten freien Nachbarn:

        neighbors_unoccupied[np.where(labeled_space != label)] = size**3
        most_restricted_within_label = neighbors_unoccupied.min()

        if most_restricted_within_label < most_restricted:
            most_restricted = most_restricted_within_label
            positions_most_restricted = np.where(
                neighbors_unoccupied == most_restricted_within_label
            )

    return np.c_[positions_most_restricted][0]   # den Erstbesten
    '''
