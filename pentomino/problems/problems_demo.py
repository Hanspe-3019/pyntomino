''' Nicht so Klassisches
'''
from .build import init

def problem_demo_all():
    ''' Demo aller 12 Steine
        Alle Steine verstreut auseinander erzeugen
    '''
    raumdemo = init((15, 15, 5))
    raumdemo[1, 1, 2] = 0     # T
    raumdemo[1:4, 2, 2] = 0
    raumdemo[1, 3, 2] = 0

    raumdemo[6, 1, 1] = 0     # F
    raumdemo[6:9, 2, 1] = 0
    raumdemo[7, 3, 1] = 0

    raumdemo[11, 1, 2] = 0    # Z
    raumdemo[11:14, 2, 2] = 0
    raumdemo[13, 3, 2] = 0

    raumdemo[1:3, 5, 3] = 0   # P
    raumdemo[1:4, 6, 3] = 0

    raumdemo[5, 5, 2] = 0     # U
    raumdemo[7, 5, 2] = 0
    raumdemo[5:8, 6, 2] = 0

    raumdemo[9:14, 5, 3] = 0  # I

    raumdemo[1, 8, 2] = 0  # L
    raumdemo[1:5, 9, 2] = 0

    raumdemo[7, 9, 1] = 0     # Y
    raumdemo[6:10, 8, 1] = 0

    raumdemo[13, 9, 3] = 0    # W
    raumdemo[12:14, 8, 3] = 0
    raumdemo[11:13, 7, 3] = 0

    raumdemo[3:5, 13, 1] = 0
    raumdemo[1:4, 12, 1] = 0

    raumdemo[7, 11, 2] = 0
    raumdemo[6:9, 12, 2] = 0
    raumdemo[7, 13, 2] = 0

    raumdemo[11, 11:13, 3] = 0
    raumdemo[11:14, 13, 3] = 0
    return raumdemo


def problem_5x6():
    'return Raum'
    raum = init((7, 9, 3))
    raum[1:6, 1:7, 1] = 0
    return raum

def problem_kreuz():
    'return Raum'
    raum = init((9, 9, 1))
    raum[3:8,  1:3, 1] = 0
    raum[1:10, 3:8, 1] = 0
    raum[3:8, 8:10, 1] = 0
    raum[5, 4:7, 1]    = -1
    raum[4:7, 5, 1]    = -1

    return raum

def problem_monster():
    'return Raum'
    raum = init((11, 7, 3))
    raum[4:9 , 1  , 1   ] = 0
    raum[1   , 2:4, 1   ] = 0
    raum[3:10, 2:4, 1   ] = 0
    raum[11, 2:4, 1     ] = 0
    raum[1:12, 4:7, 1   ] = 0
    raum[3:10, 7, 1     ] = 0
    raum[6, 4, 1] = -1
    raum[4, 5, 1] = -1
    raum[8, 5, 1] = -1

    return raum

def problem_dbl_pyramid():
    'return Raum'
    raum = init((5, 5, 5))
    raum[3:4, 3:4, 1] = 0
    raum[2:5, 2:5, 2] = 0
    raum[1:6, 1:6, 3] = 0
    raum[2:5, 2:5, 4] = 0
    raum[3:4, 3:4, 5] = 0
    return raum


def problem_pyramid():
    'return Raum'
    raum = init((5, 5, 5))

    raum[1:6, 1:6, 1] = 0
    raum[1:5, 1:5, 2] = 0
    raum[1:4, 1:4, 3] = 0
    raum[1:3, 1:3, 4] = 0
    raum[1:2, 1:2, 5] = 0
    return raum


def problem_halloween():
    'return Raum'
    raum = init((11, 7, 3))
    raum[2:11, 1, 1] = 0
    raum[1:5, 2, 1] = 0
    raum[8:12, 2, 1] = 0
    raum[1:4, 3, 1] = 0
    raum[9:12, 3, 1] = 0
    raum[1:12, 4:6, 1] = 0
    raum[2:4, 6, 1] = 0
    raum[5:8, 6, 1] = 0
    raum[9:11, 6, 1] = 0
    raum[2:6, 7, 1] = 0
    raum[7:11, 7, 1] = 0

    return raum

def problem_3x4x3():
    ' ein Vierteiler '
    raum = init((4, 3, 3))
    raum[1:5, 1:4, 1] = 0
    raum[1, 1, 1] = -1
    raum[2:4, 1:4, 2] = 0
    raum[1, 3, 2] = 0
    raum[3, 1:3, 3] = 0

    return raum

def problem_5x4x3_7():
    ' ein 7-Teiler'
    raum = init((5,4,3))

    raum[1:5, 1:5, 1] = 0
    raum[1:4, 1:5, 2] = 0
    raum[4, 1:3, 2] = 0
    raum[1, 2, 3] = 0
    raum[3, 2:4, 3] = 0
    raum[5, 1, 1:3] = 0

    return raum
