"""
MenuItem basiert auf dem gleichnamigen Tutorial-Code bei matplotlib
Ich habe den Hover-Kram allerdings entfernt. Menu wird nur über die
Tastatur bedient (siehe mesh3d.py)
"""
from dataclasses import dataclass

import matplotlib.pyplot as plt
from matplotlib.transforms import IdentityTransform

from pentomino import persist

@dataclass
class ItemProperties:
    'div. Texteigenschaften'
    fontsize: int = 10
    labelcolor: str = 'black'
    bgcolor: str = 'white'
    alpha: float = 1.0


ACTIVE = ItemProperties(labelcolor='yellow', bgcolor='black')
SELECTED = ItemProperties(labelcolor='white', bgcolor='blue')
NORMAL = ItemProperties(labelcolor='black', bgcolor='gray')

class MenuItem(plt.Rectangle):
    'beschreibt ein Menu Item'
    padx = 5
    pady = 5

    def __init__(self, fig, label_data,):
        super().__init__( (0,0), 1, 1,)

        self.set_figure(fig)
        self.problem_str, self.problem  = label_data
        self.labelstr = persist.to_menulabel(self.problem_str)
        self.is_active = False
        print(self.problem_str, self.labelstr)

        # Setting the transform to IdentityTransform() lets us specify
        # coordinates directly in pixels.
        self.label = fig.text(0, 0, self.labelstr, transform=IdentityTransform(),
                              size=NORMAL.fontsize)
        self.text_bbox = self.label.get_window_extent(
            fig.canvas.get_renderer())

        self.set_highlight(False)

    def set_extent(self, x, y, w, h, depth):
        'missing docstring'
        # pylint: disable=too-many-arguments

        self.set(x=x, y=y, width=w, height=h)
        self.label.set(position=(x + self.padx, y + depth + self.pady/2))

    def set_highlight(self, yes):
        'missing docstring'
        if self.is_active:
            return
        props = SELECTED if yes else NORMAL
        self.label.set(color=props.labelcolor)
        self.set(facecolor=props.bgcolor, alpha=props.alpha)
    def set_active(self, yes):
        ' - '
        props = ACTIVE if yes else NORMAL
        self.is_active = yes
        self.label.set(color=props.labelcolor)
        self.set(facecolor=props.bgcolor, alpha=props.alpha)
