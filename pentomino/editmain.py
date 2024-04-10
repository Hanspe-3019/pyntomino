'''
%matplotlib
'''
import matplotlib.pyplot as plt
from  matplotlib import gridspec

from pentomino.plotting import plot
from pentomino.mesh3d import Mesh3D
from pentomino.editplanes import Planes
from pentomino.problems import build
from pentomino import persist

WHITE = (1,1,1,1) # RGBA

class EditGrid:
    ''' Ein nested Grid, links Platz für 1 x 3D,
    rechts daneben eine Spalte von n Subplots

      /---------+-------------+
      |         |             |
      | Plane-0 |             |
      |---------|             |
      |         |             |
      | Plane-1 |     3D      |
      |---------|    Plot     |
      |         |             |
      | Plane-3 |             |
      |---------|             |
      |         |             |
      |   ...   |             |
      +---------+-------------/
    '''
    def __init__(self):
        self.fig = plt.figure('EditMode')
        maingrid = gridspec.GridSpec(
            1, 2,
            figure=self.fig,
            width_ratios=[3,7]
        )
        grid3d = gridspec.GridSpecFromSubplotSpec(
                1,1,
            subplot_spec=maingrid[1]
        )
        self.subplot3d = self.fig.add_subplot(
            grid3d[0],
            projection='3d',
            label='3d'
        )
        self.planes = Planes(
            self.fig,
            maingrid[0]
        )
        self.mesh3d = Mesh3D(
            self.subplot3d,
            self.planes.raum
        )

        self.cids = {
            'pick': self.fig.canvas.mpl_connect('pick_event', self.on_pick),
            'keyb': self.fig.canvas.mpl_connect('key_press_event', self.on_key),
        }

    def on_key(self, event):
        ''' Tastatureingaben werden zuerst an Planes.on_key() weitergeleitet
        Meldet die False, geht es weiter an Mesh3D.on_key().
        '''

        if event.key == 's':
            self.store_in_shelve()
        else:
            self.mesh3d.on_key(event)

    def on_pick(self, event):
        ''' Das Gitter ist pickable
        '''
        if event.mouseevent.button == 1:
            rect = event.artist
            xxx, yyy = rect.xy
            zzz = int(event.mouseevent.inaxes.get_label())
            self.planes.set_rect( (xxx, yyy, zzz), rect)
            trimmed = build.trim_with_empty_hull(self.planes.raum)
        else:
            # Verwendung der rechten oder mittlereren Maustaste
            trimmed = build.trim_with_empty_hull(self.planes.raum)
            self.planes.raum = trimmed
            self.planes.add_planes()

        self.mesh3d.refresh(trimmed)
        plot.Plot(self.subplot3d, trimmed).plot()

    def store_in_shelve(self):
        ' - '
        if self.planes.count_set < 10 or self.planes.count_set % 5 != 0:
            self.planes.put(f'?? {self.planes.count_set}')
            return
        problem = build.trim_with_empty_hull(self.planes.raum)
        its_key = persist.USER + build.hash_it(problem)
        if len(persist.get_keys(prefix=its_key)) > 0:
            self.planes.put('Problem already saved')
            return
        saved_as = persist.save(problem, prefix=its_key)
        self.planes.put(f'store_in_shelve {saved_as}')


def main():
    ' - '
    _ = EditGrid()
    plt.ioff()
    plt.show()
if __name__ == '__main__':
    main()
