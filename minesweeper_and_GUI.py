import pygame
from minesweeper import minesweeper
from GUI import *

rows=15
cols = 20
game = minesweeper(rows, cols, difficulty=0.2)
init_game(game)

run_game(game)
