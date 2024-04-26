'''
%matplotlib
'''
import matplotlib.pyplot as plt
from  matplotlib import gridspec

from pentomino.plotting import plot
from pentomino.mesh3d import Mesh3D
from pentomino.editplanes import Planes
from pentomino.problems import build, dumpproblem, rotate
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
    def __init__(self,fig=None, space=None):
        self.fig = plt.figure('EditMode') if fig is None else fig
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
            maingrid[0],
            space=space,
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
        elif event.key in 'xyz':
            self.rotate_planes(event.key)
        elif event.key == 'e':
            self.export_as_function()
        elif event.key == 'd':
            space = build.init((4,3,1))
            self.planes.add_planes(space)
            self.mesh3d.refresh(space)
            plot.Plot(self.subplot3d, space).plot()

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
            self.planes.add_planes(trimmed)

        self.mesh3d.refresh(trimmed)
        plot.Plot(self.subplot3d, trimmed).plot()

    def store_in_shelve(self):
        ' - '
        if self.planes.count_set < 10 or self.planes.count_set % 5 != 0:
            self.planes.put(f'?? {self.planes.count_set}')
            return
        problem = build.trim_with_empty_hull(self.planes.raum, reset=True)
        its_key = persist.USER + build.hash_it(problem)
        keys_in_shelve = persist.get_keys(prefix=its_key)
        if len(keys_in_shelve) > 0:
            the_key = keys_in_shelve[0]
            _ = persist.pop(the_key)
            self.planes.put(f'Problem {the_key} deleted!')
            return
        saved_as = persist.store_problem(problem)
        self.planes.put(f'store_in_shelve {saved_as}')

    def export_as_function(self):
        ' - '
        if self.planes.count_set < 10 or self.planes.count_set % 5 != 0:
            self.planes.put(f'?? {self.planes.count_set}')
            return
        problem = build.trim_with_empty_hull(self.planes.raum)
        dumpproblem.source(problem)

    def rotate_planes(self, plane):
        ' rotate 90° '
        problem = build.trim_with_empty_hull(self.planes.raum, reset=True)
        rot = rotate.rotate_it(problem, plane, by=1)
        self.planes.add_planes(rot)
        self.mesh3d.refresh(rot)
        plot.Plot(self.subplot3d, rot).plot()

def main():
    ' - '
    _ = EditGrid()
    plt.ioff()
    plt.show()
if __name__ == '__main__':
    main()
