'''
%matplotlib
'''
import threading
import matplotlib.pyplot as plt

from pentomino.plotting.plot import Plot

from pentomino.problems.problems_demo import problem_demo_all as demo_problem
from pentomino import persist
from pentomino.solving import puzzler
from pentomino import menu
from pentomino import keymap
from pentomino.solving import perfproxy as perftree

HELPBOX = {
    "facecolor": 'antiquewhite',
    "alpha": 1.,
}
COLOR_MONITORING_ON  = (.65, .25, .25)
COLOR_MONITORING_OFF = (.95, .95, .95)

CID_GO = 'go'
CID_KEY = 'key'

class Mesh3D():
    ''' Der 3D-Kram
    '''
    def __init__(self, subplot3d, raum, x_menu=None):

        fig = subplot3d.get_figure()

        self.raum = raum

        self.subplot3d = subplot3d
        self.subplot3d.set_facecolor(COLOR_MONITORING_OFF)

        self.message = fig.text(.05, .01, '', fontsize=10, color='red')

        self.plot = Plot(self.subplot3d, self.raum)
        self.plot.plot()

        self.solver = None # puzzler.Puzzler(raum)
        self.cids = {}
        self.menu = x_menu

    def on_key(self, event):
        'key_press_event Handler delegate. Return True when handled'
        if event.key in keymap.BUILTIN_MAPPINGS:
            return True

        if self.on_key_if_menu(event):
            return True

        fig = self.subplot3d.get_figure()

        if event.key in '+-' and self.solver is not None:
            resp = self.solver.adjust_interrupt(event.key == '-')
            self.put(resp)
        elif event.key in 'xyz':
            self.plot.flip_by(event.key)
            self.plot.plot()
        elif event.key in '1234567890':
            self.change_view(event.key)
        elif event.key == 'c':
            self.plot.plot(alter_colors=True)
        elif event.key == 'g':
            self.go_and_stop()
        elif event.key == 'v':
            self.toggle_monitoring()
        else:
            _ = self.subplot3d.text2D(
                .05, .7,
                '\n'.join(keymap.give_help(event.key)),
                transform=self.subplot3d.transAxes,
                bbox=HELPBOX,
            )
            fig.canvas.draw()

        return True

    def on_key_if_menu(self, event):
        'key_press_event Handler for Showroom only. Return True when handled'
        if self.menu is None:
            # test if key valid in showroom and in Edit mode
            return False

        fig = self.subplot3d.get_figure()

        if event.key in ['left', 'right']:
            self.menu.set_current_menu(event.key=='right')
            fig.canvas.draw()
        elif event.key == 'enter':
            self.setup_problem()

        elif event.key in ['up', 'down']:
            _ = self.menu.set_selected_relative(event.key == 'up')
            fig.canvas.draw()
        elif event.key == 's':
            key = persist.store_solution(self.raum)
            self.put(f'saved as {key}')

        else:
            return False

        return True

    def go_and_stop(self):
        ''' run solver in separate thread and
        interrupt solver if already running
        '''
        thread = self.cids.get(CID_GO)
        if thread is None:
            thread = threading.Thread(
                    target=self.run_solver,
            )
            self.cids[CID_GO] = thread
            self.put('running…')
            thread.start()
        else:
            self.solver.stop() # set timeout auf 0
            thread.join()
            self.solver.reset_timeout()

    def run_solver(self):
        ''' Start oder Weiterführung der Lösungssuche
        '''
        if self.solver is None:
            self.plot = Plot(self.subplot3d, self.raum)
            self.solver = puzzler.Puzzler(self.raum)

        resp = self.solver.go()
        del self.cids[CID_GO]
        self.message.set_text(resp.message)
        self.plot.plot()
        if resp.is_finish():
            self.solver = None
            self.raum[self.raum > 0] = 0

    def setup_problem(self):
        ''' Problem laden 
        '''
        thread = self.cids.get(CID_GO)
        if thread is not None:
            self.solver.stop()
            thread.join()

        item = self.menu.set_active()
        self.raum = item.problem()
        self.message.set_text('')
        self.plot = Plot(self.subplot3d, self.raum)
        self.plot.plot()
        self.solver = puzzler.Puzzler(self.raum)

    def change_view(self, key):
        ' - '
        elev, azim = keymap.KB_VIEWS.get(key, (30, -60))
        self.subplot3d.view_init(elev=elev, azim=azim, roll=0)
        self.plot.plot()

    def put(self, message):
        ''' noch etwas
        '''
        self.message.set_text(message)
        self.subplot3d.get_figure().canvas.draw()
        self.message.set_text('.')

    def refresh(self, raum):
        '''  refresh des Raumes
        '''
        self.raum = raum
        self.solver = None

    def toggle_monitoring(self):
        ' Toggle Monitoring and face_color'
        if perftree.is_enabled():
            color = COLOR_MONITORING_OFF
            perftree.disable()
        else:
            perftree.enable()
            color = COLOR_MONITORING_ON
        self.subplot3d.set_facecolor(color)
        self.put(f'Monitoring {perftree.is_enabled()}')

class StandAlone(Mesh3D):
    ' - '
    def __init__(self, raum=None):
        fig = plt.figure('3D-Kram')
        fig.set_size_inches((8,8))
        fig.set_facecolor((.9, .9, .9))
        raum = demo_problem() if raum is None else raum
        subplot3d = fig.add_subplot(111, projection='3d')
        self.fig = fig
        self.menu = menu.Menu(fig)
        self.menu.set_current_menu(1)
        super().__init__(subplot3d, raum, self.menu)

        self.cids = {
            CID_KEY: fig.canvas.mpl_connect('key_press_event', self.on_key),
        }
        self.menu_index = 0

def run():
    ' - '
    _ = StandAlone()
    plt.ioff()
    plt.show()
if __name__ == '__main__':
    run()
