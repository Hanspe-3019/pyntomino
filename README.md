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


Pressing **g** again to continue the solving process.

The solver interrupts itself if
 - a solution is found or
 - a certain time interval is expired. This time interval can be increased or decreased
by pressing **+** or **-**.

After a timeout, the thread can be continued with **g**.

<img width="500" alt="Screenshot Solution found" src="https://github.com/Hanspe-3019/pyntomino/assets/55148527/5b05f658-8fc1-45b1-bc56-bb366733b5af">


The sequence of stones gets randomised when starting the solver.
Repeating a solver run will probably yield a new solution.

## Saving solutions and displaying them

Pressing **s**-key saves the solution. 

You save solutions in a [Shelve Data Base](https://docs.python.org/3/library/shelve.html) named pentomino.db.
The default location is your home directory and can be set by setting $SHELVEDIR.
The database is created during the very first save.


If there are saved solutions for a problem, you can browse them
by pressing **j** or **k**. Pressing **d** deletes the solution from the database.

## Adding new problems
see this <a href=pentomino/problems/README.md>README</a>




