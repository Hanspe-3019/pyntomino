''' Modul mit dem ein Problem-Raum in python code verwandelt wird: 
'''
import numpy as np
def do(problem):
    ''' problem ist ein np.ndarray mit ndim=3
    '''
    print(problem.shape)
    code = [ f'    raum = init(({problem.shape})', ]

    notempty_at = np.array(np.where(problem>=0)).T
    for at in notempty_at:
        # at ist ein ndarray, ndim=1, len=3, als String '[x y z]'
        lhs = f'raum{str(at).replace(" ", ",")} = '
        rhs = f'{problem[at[0], at[1], at[2]]}'
        code.append(lhs + rhs)


    code.append('return raum')
    print('\n    '.join(code))
