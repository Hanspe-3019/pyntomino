''' Module zum initialisieren von Problemen
'''
import numpy as np

def init(dimensions):
    '''np.Array mit Rand
    '''
    xxx, yyy, zzz = dimensions
    dimensions = (xxx + 2, yyy + 2, zzz + 2)
    raum = np.zeros(dimensions, dtype=np.int8)
    raum.fill(-1)
    return raum

def trim_with_empty_hull(problem):
    ''' Erzeuge minimale Hülle um ein Problem.
    Das Problem kann teilweise oder sogar vollständig gefüllt sein
    '''
    used = (problem >= 0).nonzero() # Tuple of Arrays of Indices x, y, z

    if len(used[0]) == 0:
        # problem ist noch leer
        return problem

    x_min = used[0].min()
    y_min = used[1].min()
    z_min = used[2].min()
    x_max = used[0].max()
    y_max = used[1].max()
    z_max = used[2].max()
    trimmed = problem[
        x_min: x_max + 1,
        y_min: y_max + 1,
        z_min: z_max + 1,
    ]
    raum = np.zeros(
        np.array(trimmed.shape) + 2,
        dtype=np.int8,
    )
    raum.fill(-1)
    raum[1:-1, 1:-1, 1:-1] = trimmed
    return raum
