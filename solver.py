import numpy as np
from random import *
from math import *
from generator import *

# Solve a sodoku
def solver(sodoku):
    
    solving = True
    
    # Set the solutions dictionary
    solutions = dict()
    
    found_first_cell = False
    starting_cell = 0
    cell = 0
    square = 0
    
    for i in range(9):
        for j in range(9):
            if sodoku[i, j] == 0:
                solutions[index_to_cell(i, j)] = set()
                if not(found_first_cell):
                    cell = index_to_cell(i, j)
                    square = get_cell_stats(cell)[2]
                    found_first_cell = True
    
    # Make a set of all tried solutions
    burned = set()
    
    # Loop until a valid solution is found
    while solving:

        square = get_cell_stats(cell)[2]
        
        # Populate the solutions if we've reached a new anchor point
        if cell not in burned:
            
            taken = set()
            c = cell_to_index(cell)
            
            # Populate row solutions
            for index in range(9):
                if sodoku[c[0], index] != 0:
                    taken.add(sodoku[c[0], index])
                if sodoku[index, c[1]] != 0:
                    taken.add(sodoku[index, c[1]])
            
            # Populate the square solutions
            n = 27*floor(square/3) + (square%3) * 3
            square_cells = [n, n+1, n+2, n+9, n+10, n+11, n+18, n+19, n+20]

            for index in square_cells:
                c = cell_to_index(index)
                if sodoku[c[0], c[1]] != 0:
                    taken.add(sodoku[c[0], c[1]])

            # Add the solutions to the dictionary
            solutions[cell] = {x for x in range(1, 10)} - taken
            
            # Refresh the burned set
            burned = {x if x <= cell else -1 for x in burned}
            
            # Add the new cell to the burned solutions
            burned.add(cell)

        # Check if any solutions exist for that square
        if len(solutions[cell]) == 0:
            
            # If there are no solutions:
            
            # Clear the cell since the solution is invalid
            c = cell_to_index(cell)
            sodoku[c[0], c[1]] = 0
            
            # Remove the cell from the burned set
            burned.remove(cell)
            
            # Go back to the previous cell
            ind = list(solutions.keys()).index(cell) - 1
            cell = list(solutions.keys())[ind]
            
        else:
            
            # If solutions exist:
                      
            # Set the solution
            c = cell_to_index(cell)
            sodoku[c[0], c[1]] = list(solutions[cell])[0]
            
            # Clear the solution from the set
            solutions[cell].pop()
            
            # Find the next empty cell
            ind = list(solutions.keys()).index(cell) + 1
            
            # Terminate if at the last cell, continue otherwise
            if ind == len(solutions):
                
                # If we try to terminate with missing solutions, then the sodoku is unsolvable
                if 0 in sodoku:
                    
                    return -1
                    
                else:
                    
                    solving = False
                
            else:
            
                cell = list(solutions.keys())[ind]
        
    return sodoku
    
# Function checks to see if a sodoku solution is valid
def validator(sodoku):
    
    for i in range(9):
        present = set()
        for j in range(9):
            present.add(sodoku[i, j])
        if len(present) != 9:
            return False
            
    return True
