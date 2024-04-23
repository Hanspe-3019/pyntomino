''' Plot der 3D-Würfel eines Raums
'''
import matplotlib.pyplot as plt

import numpy as np

from pentomino.pento import get_pentominos
from pentomino.plotting import colormap
from pentomino.problems import rotate
from pentomino.problems import problems_demo as demo

PENTOMINOS = get_pentominos()

class Plot():
    ''' Zeichnet den aktuellen Zustand des Raums
    -1: Position bleibt leer, wird nicht gezeichnet
     0: Position ist noch leer, wird als weißer 3D-Würfel gezeichnet
    >0: Position ist besetzt, wird als 3D-Würfel mit der Frabe
        des Pentomino-Steins gezeichnet. 
    '''
    def __init__(self, subplot, raum, color_of_unsets='lightcoral'):
        self.fig = subplot.get_figure()
        self.subplot = subplot
        self.raum = raum

        self.flipped_by = None
        self.colors = None
        self.set_colors()
        self.color_of_unsets = color_of_unsets

        self.reset_axes()

    def refresh(self, raum):
        ' - '
        self.raum = raum
        return self

    def reset_axes(self):
        ''' doc missing
        '''
        cubes = np.array(np.where(self.raum== -1))
        min_lim = cubes.min()
        max_lim = cubes.max() + 1

        self.subplot.clear()
        self.subplot.set_xlim(min_lim, max_lim)
        self.subplot.set_ylim(min_lim, max_lim)
        self.subplot.set_zlim(min_lim, max_lim)
        self.subplot.axis('off') # dwTODO: off

    def set_colors(self):
        ''' Farben der Pentominos werden zufällig (neu) zugeordnet
        dict pentomino.typ -> Farbe
        '''
        random_colors = list(colormap.get_random_colors())
        self.colors = {
            ord(stone): random_colors[i] for i, stone in enumerate(PENTOMINOS)
        }

    def flip_by(self, plane):
        ''' Die  Darstellung wird um eine der drei Ebenen umgeklappt.

        Wir merken uns den ursprünglichen Status in `flipped_by`
        Die Übergänge sind bei der Umklapperei übersichtlich:
        x + x = None x + y = z    x + z = y
        y + x = z    y + y = None y + z = x
        z + x = y    z + y = x    z + z = None
        '''
        if self.flipped_by is None:
            self.flipped_by = plane
            return
        if self.flipped_by == plane:
            self.flipped_by = None
            return
        all_planes = list('xyz')
        all_planes.remove(plane)
        all_planes.remove(self.flipped_by)
        self.flipped_by = all_planes[0]


    def plot(self, alter_colors=False):
        '''<space> ist ein 3d-Gitter aus Würfeln:
           -1: Feld ist gesperrt und leer
           =0: Feld ist nicht gefüllt (und leer)
           >0: Feld enthält Würfel eines Pentominos
        '''

        flipped_space = (
            # Da die Lösungssuche auf Basis des nicht umgeklappten
            # Raums geschieht und diese unterbrochen wird,
            # erfolgt das Zeichnen bei geklappter Darstellung
            # auf Basis einer Kopie des Raums.

            self.raum if self.flipped_by is None else
            rotate.flip_it(self.raum, self.flipped_by)
        )
        self.reset_axes()

        if alter_colors:
            self.set_colors()

        voxels = flipped_space > 0
        if sum(voxels.flatten()) > 0:
            color_unset = (0, 0, 0, 0) # transparent
        #   https://stackoverflow.com/questions/16992713/
        #           translate-every-element-in-numpy-array-according-to-key
            uniques, inverses = np.unique(flipped_space, return_inverse=True)
            voxel_colors = np.array(
                [self.colors.get(x) for x in uniques],
                dtype=object,
                )[inverses].reshape(voxels.shape)

            self.subplot.voxels(
                voxels,
                facecolors=voxel_colors,
                edgecolors='black'
            )
        else:
            color_unset = (0.7, 0.1, 0.1, 0.7) # semi transparent

        self.subplot.voxels(
            flipped_space == 0,
            facecolors=color_unset,
            edgecolors='lightgray',
        )

        self.fig.canvas.draw()

def test():
    ''' Standalone Demo
    '''
    demo_fig = plt.figure('Demo plot.py')
    demo_subplot = demo_fig.add_subplot(111, projection='3d')
    plot = Plot(demo_subplot, demo.problem_demo_all())
    plot.plot()
    plt.show()

if __name__ == '__main__':
    test()
