''' Rund um die Tastatursteuerung im interaktiven Modus
keymap.back: ['left', 'c', 'backspace', 'MouseButton.BACK']
keymap.copy: ['ctrl+c', 'cmd+c']
keymap.forward: ['right', 'v', 'MouseButton.FORWARD']
keymap.fullscreen: ['f', 'ctrl+f']
keymap.grid: ['g']
keymap.grid_minor: ['G']
keymap.help: ['f1']
keymap.home: ['h', 'r', 'home']
keymap.pan: ['p']
keymap.quit: ['ctrl+w', 'cmd+w', 'q']
keymap.quit_all: []
keymap.save: ['s', 'ctrl+s']
keymap.xscale: ['k', 'L']
keymap.yscale: ['l']
keymap.zoom: ['o']
'''
import matplotlib

matplotlib.rcParams['keymap.grid'] = []
matplotlib.rcParams['keymap.back'].remove('left')
matplotlib.rcParams['keymap.back'].remove('c')
matplotlib.rcParams['keymap.forward'].remove('right')
matplotlib.rcParams['keymap.forward'].remove('v')
matplotlib.rcParams['keymap.save'].remove('s')
matplotlib.rcParams['keymap.home'].remove('r')
matplotlib.rcParams['keymap.xscale'] = []
matplotlib.rcParams['keymap.yscale'] = []

KB_VIEWS = {
    # https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html
    "1": (90, -90), # XY
    "2": (0, -90), # XZ
    "3": (0, 0), # YZ
    "4": (40, -40), # oben vorne rechts
    "5": (40, +50), # oben vorne links
    "6": (40, 140), # oben hinten links
    "7": (40, 230), # oben hinten rechts
    "8": (-40, -40), # von unten
    "9": (-40, +50), # von unten
    "0": (-40, 230), # von unten
}

BUILTIN_MAPPINGS = set(
    sum(
        [
            matplotlib.rcParams[mapping]
            for mapping in matplotlib.rcParams
            if mapping.startswith('keymap')
        ], []
    )
).union('shift alt control cmd'.split())

def give_help(key):
    ''' Hilfetext einblenden
    '''
    return [
        f'You pressed {key}, which is undefined.',
        f'{"\u2003"*24}',
        '   g   : Start/Interrupt and continue solving',
        '  + -  : Change interrupt interval',
        '   v   : Toggle verbose',
        ' x y z : Flip the plot around axis', 
        '  0-9  : Choose predefined view',
        '   c   : Alter colormap',
        '   s   : Save a solution to shelve file',
        '  j k  : Browse saved solutions',
     ]
