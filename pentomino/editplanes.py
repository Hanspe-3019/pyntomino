'''
%matplotlib
'''
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import ticker

from pentomino.problems import build

WHITE = (1,1,1,1) # RGBA

class Planes:
    ''' -
    '''
    def __init__(self, fig, gridplanes):
        self.fig = fig
        self.gridplanes = gridplanes
        self.raum = build.init((4,3,1))
        self.add_planes()
        self.count_set = 0

    def remove_gridplanes(self):
        ''' -
        '''
        for plane in self.fig.axes[1:]:
            plane.remove()
    def add_planes(self):
        ' - '
        self.remove_gridplanes()
        (width, height, count) = self.raum.shape

        gridedit = gridspec.GridSpecFromSubplotSpec(
            count,
            1,
            subplot_spec=self.gridplanes
        )
        i_last_plane = count - 1
        planes= [
        # Die Ebene wird mit einem Label markiert für die Picker-Logik.
        # Axis-Label ist der Text in der Legende. Weil wir keine haben,
        # bleibt das Label unsichtbar.
            self.fig.add_subplot(
                gridedit[i_last_plane  - i],
                label=str(i),
                xlim=(0,width),
                ylim=(0,height),
            ) for i in range(count)
        ]

        for i, plane in enumerate(planes):
            self.draw_mesh(plane)
            plane.set_ylabel(f'Plane {i}', fontsize='x-small')
            plane.tick_params(
                labelbottom=False,
                labeltop=( i == i_last_plane ),
                direction='in',
                labelsize='x-small',
            )
            plane.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            plane.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            if i < i_last_plane:
                plane.sharex(planes[i_last_plane])

        planes[0].set_xlabel(
            'Left click toggles selection,\nright click will trim',
            loc='left',
            fontsize='x-small'
        )

    def draw_mesh(self, subplot):
        ''' Zeichne ein Gitter
        '''
        width, height, _ = self.raum.shape
        z_val = int(subplot.get_label())
        for x_val in range(0, width):
            for y_val in range(0, height):
                facecolor = 'white' if self.raum[x_val, y_val, z_val] <  0 else 'gray'
                subplot.add_artist(
                    plt.Rectangle(
                        (x_val, y_val),
                        1,
                        1,
                        picker=True,
                        facecolor=facecolor,
                        edgecolor='black',
                    )
                )
        subplot.set_aspect(1)


    def set_rect(self, xyz, rect):
        ''' -
        '''
        xxx, yyy, zzz = xyz
        if rect.get_facecolor() == WHITE:
            self.count_set += 1
            color = 'gray'
            self.raum[xxx, yyy, zzz] = 0
        else:
            self.count_set += -1
            color = WHITE
            self.raum[xxx, yyy, zzz] = -1

        self.fig.axes[1].set_xlabel(
            f'Positionen gewählt: {self.count_set}',
            loc='left',
            fontsize='x-small'
        )
        rect.set_facecolor(color)
    def put(self, message):
        ' display message '
        self.fig.axes[1].set_xlabel(
            message,
            loc='left',
            fontsize='x-small',
        )
        self.fig.canvas.draw()
