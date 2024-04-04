''' Export space as 2D-svg
'''
import matplotlib.pyplot as plt
import numpy as np

from pentomino import persist
from pentomino.problems import build

COLORS = np.array(
    [
        [ 50,  50,  50],  # gray
        [255, 255, 255],  # white
    ]
)

def stretch_and_filter(plane, by=10):
    ''' Die Ebene wird um den Faktor `by` in beiden Dimensionen gedehnt.
    Daraus lässt sich ein 2-farbiges Image erstellen, bei dem dann die Übergänge
    in `plane` schwarz angemalt werden. 
    '''
    stretched = plane.repeat(by, axis=1).repeat(by, axis=0)
    img = np.zeros_like(stretched)
    img.fill(1)  # alles weiß
    img[np.where(stretched != np.roll(stretched, 1, axis=0))] = 0
    img[np.where(stretched != np.roll(stretched, 1, axis=1))] = 0
    # wo links und oben beides schwarz ist, ist noch weiß
    weiss = img == 1
    oben = np.roll(img, -1, axis=0) == 0
    links = np.roll(img, -1, axis=1) == 0
    img[np.roll(weiss & oben & links, 1, axis=(0, 1))] = 0

    return COLORS[
        img[by: 1-by, by: 1-by]
    ]

def draw(fig, space):
    '''  zeiche Ebenen nebeneinander '''
    space = build.trim_with_empty_hull(space)

    _, _, nplanes = space.shape

    subplots = fig.subplots(
        nrows=1,
        ncols=nplanes-2,
        squeeze=False,
    )[0]

    for i, subplot in enumerate(subplots):
        subplot.axis('off')
        img = stretch_and_filter(space[:, :, i+1])
        subplot.imshow(img, aspect='equal')

def show_plane_view(space):
    ''' Display space as tomograms along z-axis
    '''
    fig = plt.figure('Tomogram View')
    draw(fig, space)
    plt.ioff()
    plt.show()

if __name__ == '__main__':
    show_plane_view(persist.get_obj('hard_f_1'))
