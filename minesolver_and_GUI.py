from minesweeper import minesweeper
import minesolver
from GUI import *

rows=15
cols=15
difficulty=.15

ms = minesweeper(rows,cols,difficulty)
minesolver.minesolver(ms,rows,cols,difficulty)
init_game(ms)

run_game(ms)
