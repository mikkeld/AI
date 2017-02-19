# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We add constraints that the variables must satisfy. In our example we state that if two boxes in a unit contains the two same digits those two digits can only be in either of those boxes and should be eliminated from all other boxes in the unit.
The implementation consists of multiple steps:
1) Loop through all units and extract the twins (2 digits occuring twice in a given unit)
2) Loop through all boxes in the given unit and remove either digits of the twins from it's peers in the same unit
3) Returning the resulting Sudoku dictionary

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We add the diagonal units to the unitlist and our peer solution and eliminate and one choice algorithms automatically adjusts to this adding the additional two unit as constraints to our model
Most of this solution relies on prior code. The only additional implementation is adding two units (both diagonals) to the unit set.
The solved function relies on the grid_values function to transform a string input puzzle into a dictionary and we solve this using the DFS search method.
If a solution is found we return that solution. If not, we return False

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.