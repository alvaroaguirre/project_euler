# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down.
# There are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
from scipy.special import comb
grid = 20
comb(grid*2,grid,exact=True)
