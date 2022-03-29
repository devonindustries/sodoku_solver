import numpy as np
from random import *
from math import *

# Generate a sodoku with default 20 numbers to begin with
def generate_soduku(size=20):

    board = np.zeros(shape=(9,9))
    chosen = [-1]

    # Take note of the pencilled in cells
    p_rows = []
    p_cols = []
    p_squares = []

    for i in range(size):
        cell = -1
        while cell not in chosen:
            cell = randint(0,81)
        
        # Get the row, column and square containing the cell
        row = floor(cell / 9)
        col = (cell%9)
        square = floor(row/3) * 3 + floor(col/3)
        