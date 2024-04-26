''' Liste der Räume in den problems modulen und user problems
Dies Modul exportiert
MODULES_HERE : Liste der vorhandenen Problem-Module mit den vordefinierten
               Problems (ohne _MODUL_PREFIX
'''
import importlib   # https://docs.python.org/3/library/importlib.html
import inspect     # https://docs.python.org/3/library/inspect.html
from pathlib import Path

from pentomino import persist

_FUNC_PREFIX = 'problem_'
_MODUL_PREFIX = 'problems_'
_USER_PROBS = '*USER*'


class Problems():
    ''' Der Modul-Halter
    '''
    def __init__(self, modname):
        self.mod = importlib.import_module(
                '.problems.' + _MODUL_PREFIX + modname,
                package='pentomino',
                ) if modname != _USER_PROBS else None
        self.funcs = dict(
            inspect.getmembers(
                self.mod,
                inspect.isfunction
            )
        ) if modname != _USER_PROBS else None

    def get_problems(self):
        ''' Liste der in mod enthaltenen Funktionen bzw.
            Liste der Keys der User-Problems
        '''
        if self.mod is None:
            # persist.USER + SHA1 + '_0'
            # z.B. #75e1ca55cc8515f2963ef89c388ae19b8345198b_0
            return persist.get_problems_user()

        return [func.removeprefix(_FUNC_PREFIX)
                for func in self.funcs
                if func.startswith(_FUNC_PREFIX)]

    def get_problem_fkt(self, name):
        ''' liefert function object
        '''
        if self.mod is None:
            def get_obj():
                return persist.get_obj(name)

            return get_obj

        return self.funcs.get(_FUNC_PREFIX + name, None)

_USER = [_USER_PROBS,] if persist.has_problems_user() else []
MODULES_HERE = [
    module.stem.removeprefix(_MODUL_PREFIX)
    for module in Path(__file__).parent.glob('*.py')
    if module.stem.startswith(_MODUL_PREFIX)
] + _USER
