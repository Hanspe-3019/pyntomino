''' Proxy für optionales package perftree
git@github.com:Hanspe-3019/perftree.git
'''
try:
    import perftree
except ImportError:
    PROXY = False
else:
    PROXY = True

def _time_it(func):
    ' empty decorator '
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def _print_it(header='\n', footer=None):
    print(header)
    if footer is not None:
        print(footer)

class _TimeIt():
    ' empty  Context Manager'
    def __init__(self, name):
        _ = name
    def __enter__(self):
        return
    def __exit__(self, exc_type, exc_value, exc_tb):
        return

def _reset():
    return None
def _enable():
    return
def _disable():
    pass
def _is_enabled():
    return False

time_it    = perftree.time_it    if PROXY else _time_it
is_enabled = perftree.is_enabled if PROXY else _is_enabled
disable    = perftree.disable    if PROXY else _disable
enable     = perftree.enable     if PROXY else _enable
reset      = perftree.reset      if PROXY else _reset
TimeIt     = perftree.TimeIt     if PROXY else _TimeIt
print_it   = perftree.print_it   if PROXY else _print_it
