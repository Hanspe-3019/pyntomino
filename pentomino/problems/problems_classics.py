' Klassiker '

from .build import init

def problem_9x3x3():
    'return Raum'
    raum = init((9,3,3))
    raum[1:10, 1, 1:4] = 0
    raum[1:10, 3, 1:4] = 0
    raum[1, 2, 1:4] = 0
    raum[9, 2, 1:4] = 0
    return raum

def problem_5x4x3():
    'return Raum'
    raum = init((5, 4, 3))
    raum[1:6, 1:5, 1:4] = 0
    return raum

def problem_5x4x3_a():
    'return Raum'
    raum = problem_5x4x3()
    raum[1:6, 3, 2] = ord('I')
    return raum

def problem_5x4x3_b():
    'return Raum'
    raum = problem_5x4x3()
    raum[1:6, 4, 1] = ord('I')

    return raum

def problem_5x4x3_c():
    'return Raum'
    raum = problem_5x4x3()
    raum[1:6, 2, 1] = ord('I')

    return raum

def problem_5x4x3_d():
    'return Raum'
    raum = problem_5x4x3()
    raum[1:6, 4, 2] = ord('I')

    return raum

def problem_4x15():
    'return Raum'
    raum = init((4, 15, 1))
    raum.fill(-1)
    raum[1:5, 1:16, 1] = 0
    return raum

def problem_6x10():
    'return Raum'
    raum = init((6, 10, 1))
    raum.fill(-1)
    raum[1:7, 1:11, 1] = 0
    return raum
def problem_6x5x2():
    'return Raum'
    raum = init((6, 5, 2))
    raum.fill(-1)
    raum[1:7, 1:6, 1:3] = 0
    return raum

def problem_6x5x2a():
    'return Raum'
    raum = init((6, 5, 5))
    raum.fill(-1)
    raum[1:7, 1:6, 1] = 0
    raum[1:7, 1:6, 4] = 0
    return raum


def problem_8x8():
    'return Raum'
    raum = init((8, 8 , 1))
    raum.fill(-1)
    raum[1:9, 1:9, 1] = 0
    raum[3,3,1] = -1
    raum[6,3,1] = -1
    raum[3,6,1] = -1
    raum[6,6,1] = -1
    return raum

def problem_8x8_m():
    'return Raum'
    raum = init((8, 8, 1))
    raum.fill(-1)
    raum[1:9, 1:9, 1] = 0
    raum[4:6,4:6,1] = -1
    return raum

def problem_8x8_o():
    'return Raum'
    raum = init((8, 8, 1))
    raum.fill(-1)
    raum[1:9, 1:9, 1] = 0
    raum[1,1,1] = -1
    raum[1,8,1] = -1
    raum[8,1,1] = -1
    raum[8,8,1] = -1
    return raum

def problem_5x10():
    'return Raum'
    raum = init((5, 10, 1))
    raum.fill(-1)
    raum[1:6, 1:11, 1] = 0
    return raum
