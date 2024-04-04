''' Die meisten Steine können als 2x2x3 in 3D dargestellt werden:
    X und W gehen nicht, W offensichtlich nicht, weil der I-Stein
    nicht passt.
    Der F-Stein soll nur eine Lösung haben!?
'''

from pentomino.problems import build as problem

def problem_hard_f():
    '''
    F F F F
    F F F F
        F F F F
        F F F F
        F F
        F F
    '''
    raum = problem.init((6, 6, 3))
    raum[1:5, 1:3, 1:4] = 0
    raum[3:7, 3:5, 1:4] = 0
    raum[3:5, 5:7, 1:4] = 0

    return raum

def problem_hard_i():
    '''
    I I I I I I I I I I
    I I I I I I I I I I
    '''
    raum = problem.init((10, 2, 3))
    raum[1:11, 1:3, 1:4] = 0

    return raum

def problem_hard_l():
    '''
    L L 
    L L 
    L L L L L L L L 
    L L L L L L L L 
    '''
    raum = problem.init((8, 4, 3))
    raum[1:3, 1:3, 1:4] = 0
    raum[1:9, 3:5, 1:4] = 0

    return raum

def problem_hard_n():
    '''
    N N N N
    N N N N
        N N N N N N
        N N N N N N
    '''
    raum = problem.init((8, 4, 3))
    raum[1:5, 1:3, 1:4] = 0
    raum[3:9, 3:5, 1:4] = 0

    return raum

def problem_hard_p():
    '''
    P P P P P P 
    P P P P P P 
    P P P P   
    P P P P   
    '''
    raum = problem.init((6, 4, 3))
    raum[1:7, 1:3, 1:4] = 0
    raum[1:5, 3:5, 1:4] = 0

    return raum

def problem_hard_t():
    '''
    T T T T T T
    T T T T T T
        T T
        T T
        T T
        T T
    '''
    raum = problem.init((6, 6, 3))
    raum[1:7, 1:3, 1:4] = 0
    raum[3:5, 3:7, 1:4] = 0

    return raum

def problem_hard_u():
    '''
    U U U U U U
    U U U U U U
    U U     U U
    U U     U U
    '''
    raum = problem.init((6, 4, 3))
    raum[1:7, 1:3, 1:4] = 0
    raum[1:3, 3:5, 1:4] = 0
    raum[5:7, 3:5, 1:4] = 0

    return raum

def problem_hard_v():
    '''
    V V 
    V V 
    V V 
    V V 
    V V V V V V 
    V V V V V V 
    '''
    raum = problem.init((6, 6, 3))
    raum[1:3, 1:5, 1:4] = 0
    raum[1:7, 5:7, 1:4] = 0

    return raum

def problem_hard_y():
    '''
        Y Y
        Y Y 
    Y Y Y Y Y Y Y Y 
    Y Y Y Y Y Y Y Y 
    '''
    raum = problem.init((8, 4, 3))
    raum[3:5, 1:3, 1:4] = 0
    raum[1:9, 3:5, 1:4] = 0

    return raum

def problem_hard_z():
    '''
    Z Z Z Z
    Z Z Z Z
        Z Z
        Z Z
        Z Z Z Z
        Z Z Z Z
    '''
    raum = problem.init((6, 6, 3))
    raum[1:5, 1:3, 1:4] = 0
    raum[3:5, 3:5, 1:4] = 0
    raum[3:7, 5:7, 1:4] = 0

    return raum
# ------------------------------ #
def problem_treppe():
    '''
    X
    X X
    X X X
    X X X X
    X X X X X
    vier tief!
    '''
    raum = problem.init((5, 4, 5))
    raum[1:6, 1:5, 1] = 0
    raum[1:5, 1:5, 2] = 0
    raum[1:4, 1:5, 3] = 0
    raum[1:3, 1:5, 4] = 0
    raum[1:2, 1:5, 5] = 0
    return raum
