import minesolver
from minesweeper import minesweeper
rows=15
cols=15
difficulty=.15
game = minesweeper(rows,cols,difficulty)
minesolver.minesolver(game,rows,cols,difficulty)
