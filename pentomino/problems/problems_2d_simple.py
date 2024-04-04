''' Je Pentomino ein Puzzle des Pentonminos waagerecht dreifach vergrößert:
    also 9 Steine
'''

from .build import init

def problem_simple_f():
    '''
              F F F F F F
              F F F F F F
              F F F F F F
        F F F F F F
        F F F F F F     f f
        F F F F F F   f f
              F F F     f
              F F F
              F F F
    '''
    raum = init((10, 9, 1))
    raum[4:10, 1:4, 1] = 0
    raum[1:7, 4:7, 1] = 0
    raum[4:7, 7:10, 1] = 0

    raum[9:11, 5, 1] = 0
    raum[8:10, 6, 1] = 0
    raum[9, 7, 1] = 0

    return raum

def problem_simple_i():
    '''
        .
        . . . . n n n n n
        .
        N N N N N N N N N N N N N N N
        N N N N N N N N N N N N N N N
        N N N N N N N N N N N N N N N
    '''
    raum = init((15, 6, 1))
    raum[1:16, 4:7, 1] = 0

    raum[5:10, 2, 1] = 0

    return raum

def problem_simple_l():
    '''
        N N N    n
        N N N    n n n n
        N N N
        N N N N N N N N N N N N
        N N N N N N N N N N N N
        N N N N N N N N N N N N
    '''
    raum = init((12, 6, 1))
    raum[1:4, 1:4, 1] = 0
    raum[1:13, 4:7, 1] = 0

    raum[6, 1, 1] = 0
    raum[6:10, 2, 1] = 0

    return raum

def problem_simple_p():
    '''
        P P P P P P   p p
        P P P P P P   p p p
        P P P P P P
        P P P P P P P P P
        P P P P P P P P P
        P P P P P P P P P
    '''
    raum = init((12, 6, 1))
    raum[1:7, 1:4, 1] = 0
    raum[1:10, 4:7, 1] = 0

    raum[8:10, 1, 1] = 0
    raum[8:11, 2, 1] = 0

    return raum

def problem_simple_n():
    '''
        N N N N N N   n n
        N N N N N N     n n n
        N N N N N N
              N N N N N N N N N
              N N N N N N N N N
              N N N N N N N N N
    '''
    raum = init((12, 6, 1))
    raum[1:7, 1:4, 1] = 0
    raum[4:13, 4:7, 1] = 0

    raum[8:10, 1, 1] = 0
    raum[9:12, 2, 1] = 0

    return raum

def problem_simple_t():
    '''
        T T T T T T T T T
        T T T T T T T T T
        T T T T T T T T T
              T T T
              T T T
              T T T t t t
              T T T   t
              T T T   t
              T T T
    '''
    raum = init((9, 9, 1))
    raum[1:10, 1:4, 1] = 0
    raum[4:7, 4:10, 1] = 0

    raum[7:10, 6, 1] = 0
    raum[8, 7:9, 1] = 0

    return raum


def problem_simple_u():
    '''
        U U U       U U U
        U U U       U U U
        U U U       U U U  u   u
        U U U U U U U U U  u u u
        U U U U U U U U U
        U U U U U U U U U
    '''
    raum = init((9+4, 6, 1))
    raum[1:4, 1:7, 1] = 0
    raum[7:10, 1:7, 1] = 0
    raum[4:7, 4:7, 1] = 0
    raum[11:14, 4:6, 1] = 0
    raum[12, 4, 1] = -1

    return raum


def problem_simple_v():
    '''
        V V V
        V V V   v
        V V V   v
        V V V   v v v
        V V V
        V V V
        V V V V V V V V V
        V V V V V V V V V
        V V V V V V V V V
    '''
    raum = init((9, 9, 1))
    raum[1:4, 1:10, 1] = 0
    raum[4:10, 7:10, 1] = 0

    raum[5, 2:5, 1] = 0
    raum[6:8, 4, 1] = 0

    return raum

def problem_simple_w():
    '''
        W W W W W W
        W W W W W W
        W W W W W W
              W W W W W W
              W W W W W W
              W W W W W W
        w w         W W W
          w w       W W W
            w       W W W
    '''
    raum = init((9, 9, 1))
    raum[1:7, 1:4, 1] = 0
    raum[4:10, 4:7, 1] = 0
    raum[7:10, 7:10, 1] = 0
    raum[1:3, 7, 1] = 0
    raum[2:4, 8, 1] = 0
    raum[3, 9, 1] = 0

    return raum

def problem_simple_x():
    '''
              X X X
              X X X
              X X X
        X X X X X X X X X
        X X X X X X X X X
        X X X X X X X X X
              X X X
              X X X     x
              X X X   x x x
                        x
    '''
    raum = init((10, 10, 1))
    raum[4:7, 1:10, 1] = 0
    raum[1:10, 4:7, 1] = 0

    raum[9, 8:11, 1] = 0
    raum[8:11, 9, 1] = 0

    return raum

def problem_simple_y():
    '''
        Y Y Y
        Y Y Y
        Y Y Y
        Y Y Y Y Y Y
        Y Y Y Y Y Y
        Y Y Y Y Y Y
        Y Y Y
        Y Y Y   y
        Y Y Y   y y
        Y Y Y   y
        Y Y Y   y
        Y Y Y
    '''
    raum = init((6, 12, 1))
    raum[1:4, 1:13, 1] = 0
    raum[4:7, 4:7, 1] = 0

    raum[5, 8:12, 1] = 0
    raum[5:7, 9, 1] = 0

    return raum

def problem_simple_z():
    '''
        Z Z Z Z Z Z
        Z Z Z Z Z Z
        Z Z Z Z Z Z
              Z Z Z
        z z   Z Z Z
          z   Z Z Z
          z z Z Z Z Z Z Z
              Z Z Z Z Z Z
              Z Z Z Z Z Z
    '''
    raum = init((9, 9, 1))
    raum[4:7, 1:10, 1] = 0
    raum[1:4, 1:4, 1] = 0
    raum[7:10, 7:10, 1] = 0

    raum[2, 5:8, 1] = 0
    raum[1, 5, 1] = 0
    raum[3, 7, 1] = 0

    return raum
