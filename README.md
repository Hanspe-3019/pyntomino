# Pentominos are fun

A Solver for [Pentomino](https://en.wikipedia.org/wiki/Pentomino) 2D- and 3D-puzzles written in python using 
[matplotlib's interactive backend](https://matplotlib.org/stable/users/explain/figure/backends.html).

Beside [numpy](https://numpy.org) the solver also uses [scikit-image's morphology](https://scikit-image.org/docs/stable/api/skimage.morphology.html)

The package contains some builtin puzzle problems. Via Edit Mode new problems can be created and saved as *User Problems*.

Found solutions of builtin and user problems can be saved.

## Install

Clone or download the repo and go into directory with setup.py. Run
```bash
pip install .
```
## How to use


Starting from the shell, you can use the package in two modes: *Showroom* and *Editmode*.

The puzzle is shown as 3D-projection. The view can be adjusted by dragging with the mouse. Predefined views can be applied via keyboard keys `0` to `9`. 
The display can also be adjusted by 
flipping along one axis via keyboard keys `x`, `y`, `z`.

The colors used to display and the pentominos are choosen at random and
can be altered via keyboard key `c`.

### Showroom
Show and solve predefined and user problems. To run enter 
```bash
python -m pentomino
```
<img width="500" alt="Screenshot Puzzle to be solved" src="https://github.com/Hanspe-3019/pyntomino/assets/55148527/20806250-3040-4c8c-ac62-7329fc90ddd7">

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
<img width="500" alt="Screenshot Editmode" src="https://github.com/Hanspe-3019/pyntomino/assets/55148527/3125270f-a2b0-4f61-b5fc-0880d6beae9e">

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

<img width="500" alt="Screenshot Solver timed out" src="https://github.com/Hanspe-3019/pyntomino/assets/55148527/1a20c1f8-715c-40d6-a44c-84792563e7e6">


Pressing **g** again to resume the solving process.

The solver interrupts itself if

 - a solution is found or
 - a certain time interval is expired. This time interval can be increased or decreased
by pressing **+** or **-**.

After an interrupt, the thread can be continued with **g**.

<img width="500" alt="Screenshot Solution found" src="https://github.com/Hanspe-3019/pyntomino/assets/55148527/5b05f658-8fc1-45b1-bc56-bb366733b5af">


The sequence of stones gets randomised when starting the solver.
Repeating a solver run will probably yield another solution.

## Saving solutions and displaying them

Pressing **s**-key in Showroom saves the solution.

Pressing **s**-key in Editmode saves the problem. 

The saved data is saved in a [Shelve Data Base](https://docs.python.org/3/library/shelve.html) named **pentomino.db**.
The default location is your home directory and can be set by setting $SHELVEDIR.
The database is created during the very first save.


If there are saved solutions for a problem, you can browse them in Showroom 
by pressing **j** or **k**. Pressing **d** deletes the solution from the database.

## Adding or modifying builtin problems
This is to be done by coding simple python functions, you can also add or modify the structure
of the menues by sorting problem functions into problem modules.
see this <a href=pentomino/problems/README.md>README</a>

## Saving user problems

Start Editmode with `python -m pentomino --edit`.

Build a new problem by clicking the fields on the planes.

When satisfied, press key **s** to save the problem into *pentomino.db*.

The internal data that describes your problem is hashed to create a unique key to store it in *pentomino.db*.

All user problems are selectable in Showroom's menu as special problem group and can be used like builtin problems.

## Removing a user problem

In Showroom activate the problem to be removed and press key **d**. 

If there are already solutions stored, these have to be deleted first.


