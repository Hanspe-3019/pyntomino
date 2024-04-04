''' main module.
This is executed when running `python -m pentonmino`
'''
import sys

from pentomino import editmain
from pentomino import showroom

USAGE = '''
run with 
    python -m pentomino
to solve predefined problems or
    python -m pentomino --edit
to build your own problems.
'''
def main():
    ' - '
    if len(sys.argv) == 2 and sys.argv[1] in '-e --edit'.split():
        editmain.main()
    elif len(sys.argv) == 1:
        showroom.main()
    else:
        print(USAGE)

main()
