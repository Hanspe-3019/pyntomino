''' Anzeige der gespeicherten Pentominos
'''
import matplotlib.pyplot as plt

from pentomino.mesh3d import Mesh3D
from pentomino import persist
from pentomino import menu
from pentomino.plotting import draw2d
from pentomino.problems.problems_demo import problem_demo_all as demo_problem

def main():
    ' - '
    _ = Showroom()

    plt.ioff()
    plt.show()

class Showroom(Mesh3D):
    ' - '
    def __init__(self):
        fig = plt.figure('Showroom')
        fig.set_size_inches((8,8))
        fig.set_facecolor((.9, .9, .9))
        raum = demo_problem()
        subplot3d = fig.add_subplot(111, projection='3d')
        self.fig = fig
        self.menu = menu.Menu(fig)
        self.menu.set_current_menu(1)
        self.saved_versions = []    # [(key, space)]
        self.current = 0
        super().__init__(subplot3d, raum, self.menu)

        self.cids = {
            'key': fig.canvas.mpl_connect(
                'key_press_event', self.my_on_key
                ),
        }
        self.menu_index = 0


    def my_on_key(self, event):
        ''' Tasten, die hier nicht verarbeitet werden, 
        werden an die Mutter weitergeleitet.
        z.B. wählt ← oder → eine Problemgruppe aus,
        das macht Mesh3D.on_key()
        z.B. wählt j oder k eine Historie aus der Shelve aus,
        eine Aufgabe für den Showroom
        '''
        if event.key in ['left', 'right']:
            # Menu-Wechsel
            super().on_key(event)
            self.current = -1
        elif event.key == 'enter':
            # Auswahl eines Problems:  Anzeige des Problems
            super().on_key(event)
            item = self.menu.get_selected()
            self.current = -1
            self.saved_versions = persist.get_versions(item.labelstr)
            self.fig.suptitle(
                'No Solutions yet' if len(self.saved_versions) == 0 else
                f'{len(self.saved_versions)} Solutions stored'
            )
            self.fig.canvas.draw()
        elif event.key in 'kj':
            # Bewegung in den Lösungen zu einem Problem
            if len(self.saved_versions) == 0:
                return
            incr = 1 if event.key == 'j' else -1
            self.current = (self.current + incr) % len(self.saved_versions)
            self.fig.suptitle(
                f'{self.current+1} from {len(self.saved_versions)}'
            )
            _, current_space = self.saved_versions[self.current]
            self.refresh(current_space)
            self.plot.refresh(current_space).plot()
        elif event.key == 't':
            plt.close('Tomogram View')
            fig_2d = plt.figure('Tomogram View')
            draw2d.draw(fig_2d, self.raum)
            fig_2d.show()

        elif event.key == 's':
            # nach save noch refresh von self.spaces
            super().on_key(event)
            item = self.menu.get_selected()
            self.saved_versions = persist.get_versions(item.labelstr)

            self.fig.suptitle(
                f'{len(self.saved_versions)} Solutions stored'
            )

        elif event.key == 'd':
            try:
                version_key, _ = self.saved_versions[self.current]
            except IndexError: # Delete problem
                item = self.menu.get_selected()
                _ = persist.pop(item.problem_str)
                if item.problem_str.startswith(persist.USER):
                    self.menu.refresh()
                    self.put(f'removed {item.problem_str}')
                    _ = self.menu.set_selected_relative(None)
                    self.setup_problem()
                else:
                    self.put('Only user problems can be deleted')
            else: # Delete version
                _ = persist.pop(version_key)
                self.saved_versions.pop(self.current)
                self.put(f'removed {version_key}')
        else:
            super().on_key(event)

if __name__ == '__main__':
    main()
