''' Probleme maus 3d_hard mit Vorbesetzungen
    die funktionsnamen sind die selben. Dadurch
    werden Lösungen zwischen den beiden Varianten geteilt.
'''

from pentomino.problems import build as problem
from pentomino.problems import problems_3d_hard as raw

def problem_hard_f():
    '''
        U X F F
        U F F F
            F F F F
            F F F F
            F F
            F F
    '''
    raum = raw.problem_hard_f()

    # U und X vorbesetzen
    raum[2, 1, 1] = ord('X')  # X
    raum[1, 1, 2] = ord('X')  # X
    raum[2, 1, 2] = ord('X')  # X
    raum[3, 1, 2] = ord('X')  # X
    raum[2, 1, 3] = ord('X')  # X
    raum[1, 1, 1] = ord('U')  # U
    raum[1, 2, 1] = ord('U')  # U
    raum[1, 2, 2] = ord('U')  # U
    raum[1, 2, 3] = ord('U')  # U
    raum[1, 1, 3] = ord('U')  # U

    return raum

def problem_hard_l():
    ''' Vorbetzt mit Y L W
    '''
    raum = raw.problem_hard_l()

    raum[1, 2:4, 3] = ord('W')
    raum[2, 3:5, 3] = ord('W')
    raum[3, 4, 3]   = ord('W')
    raum[5:9, 3, 3] = ord('Y')
    raum[7, 3, 2]   = ord('Y')
    raum[5:9, 3, 1] = ord('L')
    raum[8, 3, 2]   = ord('L')

    return raum

def problem_hard_n():
    ' - '

    raum = raw.problem_hard_n()

    return raum

def problem_hard_p():
    ' - '

    raum = raw.problem_hard_p()

    raum[1:4, 1, 1] = ord('V')
    raum[1, 1, 2 ]  = ord('V')
    raum[1, 1, 3 ]  = ord('V')
    raum[4:6, 1, 1] = ord('N')
    raum[2:5, 1, 2] = ord('N')
    raum[1, 4, 1  ] = ord('Z')
    raum[1, 2:5, 2] = ord('Z')
    raum[1, 2, 3  ] = ord('Z')

    return raum

def problem_hard_t():
    ''' Vorbesetzen mit F Y l
    '''
    raum = raw.problem_hard_t()
    raum[1:5, 1, 1] = ord('Y')
    raum[2, 2, 1] = ord('Y')
    raum[5, 1, 1] = ord('F')
    raum[3:6, 2, 1] = ord('F')
    raum[4, 3, 1]  = ord('F')
    raum[3, 3:7, 1] = ord('L')
    raum[3, 6, 2] = ord('L')

    return raum

def problem_hard_w():
    '''
    W W W W
    W W W W
        W W W W
        W W W W
            W W
            W W
    '''
    raum = problem.init((6, 6, 3))
    raum[1:5, 1:3, 1:4] = 0
    raum[3:7, 3:5, 1:4] = 0
    raum[5:7, 5:7, 1:4] = 0
    raum[5,1,1] = 0
    raum[4,1,3] = -1
    raum[1:6, 1, 1] = ord('I')

    return raum


def problem_hard_y():
    ''' Vorbesetzt L N P
    '''
    raum = raw.problem_hard_y()


    raum[1:3, 3, 3] = ord('N')
    raum[2:5, 4, 3] = ord('N')
    raum[5:9, 3, 3] = ord('L')
    raum[8, 4, 3] = ord('L')
    raum[3, 1, 1] = ord('V')
    raum[3, 1, 2] = ord('V')
    raum[3, 1:4, 3] = ord('V')
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
    raum = raw.problem_treppe()
    raum[4:6, 4, 1] = ord('W')
    raum[3:5, 4 ,2] = ord('W')
    raum[3, 4, 3  ] = ord('W')
    raum[1:4, 4, 1] = ord('T')
    raum[2, 4, 2  ] = ord('T')
    raum[2, 4, 3  ] = ord('T')
    raum[1, 2:5, 5] = ord('V')
    raum[1, 4, 4  ] = ord('V')
    raum[1, 4, 3  ] = ord('V')

    return raum
