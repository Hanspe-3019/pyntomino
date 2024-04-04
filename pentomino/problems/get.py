''' Liste der Räume in den problems files
'''
import importlib   # https://docs.python.org/3/library/importlib.html
import inspect     # https://docs.python.org/3/library/inspect.html
from pathlib import Path

FUNCTION_PREFIX = 'problem_'
MODULE_PREFIX = 'problems_'

MODULES_HERE = [
    module.stem.removeprefix(MODULE_PREFIX)
    for module in Path(__file__).parent.glob('*.py')
    if module.stem.startswith(MODULE_PREFIX)
]



class Problems():
    ''' Der Modul-Halter
    '''
    def __init__(self, modname):
        self.mod = importlib.import_module(
                '.problems.' + MODULE_PREFIX + modname,
                package='pentomino',
                )
        self.funcs = dict(
            inspect.getmembers(
                self.mod,
                inspect.isfunction
            )
        )
    def get_problems(self):
        ''' Liste der in mod enthaltenen Funktionen
        '''
        return [func.removeprefix(FUNCTION_PREFIX)
                for func in self.funcs
                if func.startswith(FUNCTION_PREFIX)]

    def get_problem(self, name):
        ''' liefert function object
        '''
        return self.funcs.get(FUNCTION_PREFIX + name, None)

def test():
    ' Test '
    problems = Problems('problems')
    print(
        '\n'.join(problems.get_problems())
    )
    print(problems.get_problem('simple_f')) # gibt es
    print(problems.get_problem('simple_q')) # gibt es nicht
