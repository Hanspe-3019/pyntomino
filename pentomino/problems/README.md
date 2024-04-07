Subpackage `problems` contains the predefined problems and related utils.

The problems found here define showroom's menu:

A problem is implemented as a python function, that returns a 3-dimensional
numpy array filled with integers. 
It is possible, that a problem is prefilled with one or more pentonminos. 

 - -1 means: position has to stay empty
 -  0 means: position is a puzzle position, that is, it has to be occupied with some pentomino
 - \>0 means: position is already occupied with some part of a pentomino  <br>
The integer must be a valid numerical pentomino code.


Example: This is the function that defines the classical 5x4x3 rectangular cuboid:

```python
from .build import init # init empty problem of given dimensions+2

def problem_5x4x3():
    'return Raum'
    raum = init((5, 4, 3))
    raum[1:6, 1:5, 1:4] = 0
    return raum
```

These functions have a name prefixed with `problem_` and are defined in a module
whose name is prefixed with `problems_`.
The functions defined in the same problem module build a function group.

Example: `problem_5x4x3()` is defined in module `problems_classics.py`.

Showroom's menu is constructed by introspection of all modules `problems_*.py`
in subpackage `pentomino.problems`, see module `problems/get.py`.




 
