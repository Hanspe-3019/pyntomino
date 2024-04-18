''' Modul mit dem ein Problem-Raum in python code verwandelt wird: 
'''
def source(problem):
    ''' -
    '''
    print('def problem_<name>():')
    print('    " - "')
    code = repr(problem).split('\n')
    print(f'    return np.{code[0]}')
    print('    ' + '\n    '.join(code[1:]))
