from minesweeper import minesweeper

ms = minesweeper(10,10,0.25)

ms.print_minefield()
ms.print_board()
gameover=False
while(not gameover):
    t,i,j = input().split(" ")
    if(t=="t"):
        gameover = ms.test(int(i),int(j))
    else:
        ms.flag(int(i),int(j))
    ms.print_gameboard()
    # print(ms.gameboard)