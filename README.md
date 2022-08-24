# Sodoku Solver
 
### A Sodoku Generator and Solver that uses the back-tracking algorithm. 

To start, we can import everything that we need using the following lines of code. Note that NumPy matrices are used to represent Sodokus. An example of generating and solving a Sodoku is given below.

```
from generator import *
from solver import *

sodoku = generate_sodoku(size=23)
solved_sodoku = solver(sodoku)
```

This will store a completely solved sodoku inside the `solved_sodoku` variable. Note that if a sodoku cannot be solved, then the `solver function` will return `-1`. Not all blank sodokus can be solved, so generally it is wise to set the blank sodoku size to 23 (default).

The `generate_sodoku` algorithm will return -1 if size exceeds 81.

Alternatively, the user may supply the solver function with their own sodoku in the form of a NumPy matrix to solve.