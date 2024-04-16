"""
Menu basiert auf dem gleichnamigen Tutorial-Code bei matplotlib
Ich habe den Hover-Kram allerdings entfernt. Menu wird nur über die
Tastatur bedient (siehe mesh3d.py)
"""
import matplotlib.pyplot as plt

from pentomino.problems import get as gp
from pentomino.menuitem import MenuItem

class Menu:
    'missing docstring'
    def __init__(self, fig):
        self.fig = fig

        self.menuitems = []
        self.selected_item_index = -1
        self.active_item_index = -1
        self.current_menu = 0
    def draw_items(self):
        ' - '

        maxw = max(item.text_bbox.width for item in self.menuitems)
        maxh = max(item.text_bbox.height for item in self.menuitems)
        depth = max(-item.text_bbox.y0 for item in self.menuitems)

        (_, fig_height) = self.fig.canvas.get_width_height(physical=True)
        x0 = 10
        y0 = fig_height - 120

        width = maxw + 2*MenuItem.padx
        height = maxh + MenuItem.pady

        for item in self.menuitems:
            left = x0
            bottom = y0 - maxh - MenuItem.pady

            item.set_extent(left, bottom, width, height, depth)
            item.set_picker(True)

            self.fig.artists.append(item)
            y0 -= maxh + MenuItem.pady
    def remove(self):
        ' Menu entfernen '
        # Eine schwere Geburt, remove geht nicht für Menu.item
        # Der Hintergrund lässt sich mit set_visible entfernen
        # Die figure.artists wird auch nicht automatisch bereinigt.
        for item in self.menuitems:
            item.set_visible(False)
            item.label.remove()
        self.fig.artists.clear()

        self.fig.canvas.draw()

    def get_selected(self):
        ' - '
        return self.menuitems[self.selected_item_index]

    def set_active(self):
        ' - '
        index = self.selected_item_index
        item_active = self.menuitems[index]

        try:
            item_old = self.menuitems[self.active_item_index]
        except IndexError:
            pass
        else:
            item_old.set_active(False)

        self.active_item_index = index
        item_active.set_active(True)

        return item_active

    def set_selected_relative(self, up):
        ' - '
        incr = 0 if up is None else -1 if up else 1
        index = (self.selected_item_index + incr) % len(self.menuitems)
        item_selected = self.menuitems[index]

        try:
            item_old = self.menuitems[self.selected_item_index]
        except IndexError:
            pass
        else:
            item_old.set_highlight(False)

        item_selected.set_highlight(True)
        self.selected_item_index = index

        return item_selected

    def set_current_menu(self, up):
        ' Update menuindex'
        incr = 1 if up else -1
        self.current_menu = (
                self.current_menu + incr
                ) % len(gp.MODULES_HERE)
        self.refresh()

    def refresh(self):
        ''' Neuaufbau des Menus 
        '''
        self.remove()
        problems = gp.Problems(gp.MODULES_HERE[self.current_menu])
        self.menuitems.clear()

        for problem_str in problems.get_problems():
            problem_fkt = problems.get_problem_fkt(problem_str)
            item = MenuItem(
                self.fig,
                (problem_str, problem_fkt),
            )
            self.menuitems.append(item)

        self.draw_items()


def testit():
    ''' Test
    '''
    fig = plt.figure()

    mmm = Menu(fig)
    mmm.set_current_menu('>')

    plt.show()

if __name__ == '__main__':
    testit()
