'''Wir brauchen für die 12 Steine 12 Basisfarben.
Weil wir mit matplotlib malen, holen wir uns von dort als random sample.
'''
import random
from matplotlib import colormaps
import matplotlib.pyplot as  plt

TAB20B = colormaps['tab20b'].colors

def get_random_colors(anzahl=12):
    '''Wähle <anzahl> Farben aus dem Topf
    '''
    return random.sample(TAB20B, k=anzahl)

def draw(colors):
    ''' plt demo der Farben
    '''
    fig = plt.figure('Demo der Farben')
    subplot = fig.subplots()
    subplot.axis('off')
    rect_size = 1 / len(colors)
    for i, rgb_tuple in enumerate(colors):
        col = i/len(colors)
        subplot.add_artist(

            plt.Rectangle(
                (.1, col),
                rect_size,
                rect_size,
                facecolor=rgb_tuple
                )
        )
        rgb_str = (
            'rgb'    
            f'=({rgb_tuple[0]:.2f}'
            f', {rgb_tuple[1]:.2f}'
            f', {rgb_tuple[2]:.2f}'
            ')'
        )
        subplot.text(.3, col + rect_size/2, rgb_str, fontsize=10,
                horizontalalignment='left',
                verticalalignment='center')

    plt.ioff()
    plt.show()

if __name__ == '__main__':
    draw(get_random_colors())
