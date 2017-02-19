from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    smallest = [k for k in sorted(values, key=lambda k: len(values[k])) if len(values[k]) > 1][0]


    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[smallest]:
        new_sudoko = values.copy()
        new_sudoko[smallest] = value
        attempt = search(new_sudoko)
        if attempt:
            return attempt

    # If you're stuck, see the solution.py tab!