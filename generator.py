import numpy as np
from random import *
from math import *

# Generate a sodoku with default 20 numbers to begin with
def generate_sodoku(size=20):

    board = np.zeros(shape=(9,9))
    p_board = [[set() for x in range(9)] for y in range(9)]

    # Fill in a random cell
    cell = randint(0, 80)
    value = randint(1, 9)

    c = cell_to_index(cell)
    board[c] = value
    p_board[c[0]][c[1]] = -1

    # Fill in the remaining cells
    for i in range(1, size):
        
        # Get the possible locations of the next few numbers
        row, col, square = get_cell_stats(cell)

        # Fill the pencil cells in
        for index in range(9):

            # Rows
            if p_board[row][index] == -1:
                pass
            else:
                p_board[row][index].add(value)
                
            # Columns
            if p_board[index][col] == -1:
                pass
            else:
                p_board[index][col].add(value)

        # Fill in the square pencil cells
        n = 27*floor(square/3) + (square%3) * 3
        square_cells = [n, n+1, n+2, n+9, n+10, n+11, n+18, n+19, n+20]

        for s_cell in square_cells:
            c = cell_to_index(s_cell)

            if p_board[c[0]][c[1]] == -1:
                pass
            else:
                p_board[c[0]][c[1]].add(value)
                
        # Fill in a random pencilled in cell
        c = cell_to_index(cell)
        flag = True
        while flag:
            if type(p_board[c[0]][c[1]]) == set:
                if len(p_board[c[0]][c[1]]) != 9:
                    vals = {x for x in range(1,10)} - p_board[c[0]][c[1]]
                    value = choice(list(vals))
                    flag = False
            cell = randint(0,80)
            c = cell_to_index(cell)

        board[c] = value
        p_board[c[0]][c[1]] = -1

    return board
        

def get_cell_stats(cell):

    row = floor(cell / 9)
    col = (cell%9)

    return(
        row, # Row containing the cell
        col, # Column containing the cell
        floor(row/3) * 3 + floor(col/3) # Square containing the cell
    )

def cell_to_index(cell):
    return(floor(cell/9), cell%9)
