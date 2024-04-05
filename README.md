# Pentominos are fun

## Install

Clone repo and go into directory with setup.py. Run
```bash
pip install .
```
## How to use

You can usage the package in two modes: *Showroom* and *Editmode*: 
### Showroom
Playing with predefined problems. To run enter 
```bash
python -m pentomino
```

Figure shows a 3D subplot of the actual puzzle problem.

At the left side there is a simple menu of predefined problems.
The problems are grouped to reduce the size of the menu.

The menu is navigated with the keyboard:
 - up and down move the highlight up and down
 - enter will select the highlighted problem and will draw it as 3D projection.
 - left and right will switch the group of problems shown.

Once a problem ist selected with enter key, start the solving with the key g.
See solving below.

### Editmode
Build new problems and solve them. Run with
```bash
python -m pentomino --edit
```

The figure consists of two columns:

 - The left-hand column shows a stack of rectangular layers with fields that can be filled with the mouse.
 - The right-hand column shows the resulting 3D projection.

Left-clicking a field in the plane toggles field's fill on and off.

If a field is filled at the edge of a plane, right-click will expand the planes.

If a field in the upper or lower plane is filled, another plane is inserted at the top or bottom of the stack.  



## Solving
Once a problem is selected, enter **g** to start the solver.
The solver is executed as a separate Python thread
and can be interrupted with another press of **g**.

Pressing **g** again to continue the solving process.

The solver interrupts itself if
 - a solution is found or
 - a certain time interval is expired. This time interval can be increased or decreased
by pressing **+** or **-**.

After a timeout, the thread can be continued with **g**.

The sequence of stones gets randomised when starting the solver.
Repeating a solver run will probably yield a new solution.

## Saving solutions and displaying them

Pressing **s**-key saves the solution. 

https://docs.python.org/3/library/shelve.html

You save solutions in a Shelve Data Base named pentomino.db.
The default location is your home directory and can be set by setting $SHELVEDIR.
The database is created during the very first save.


If there are saved solutions for a problem, you can browse them
by pressing **j** or **k**. Pressing **d** deletes the solution from the database.

## Adding new problems




