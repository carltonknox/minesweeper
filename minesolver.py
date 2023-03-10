from minesweeper import minesweeper
import random
# random.seed(1000158)
rows=10
cols=15
difficulty=.15
ms = minesweeper(rows,cols,difficulty)
gameover=False
while(not gameover):
    #First check for completion
    gameover = not any("?" in c for c in ms.gameboard)
    if(gameover):
        continue
    #copy gameboard
    # gb = [row[:] for row in ms.gameboard]
    found=False
    #First, check for any obvious solutions (ie 1 with only 1 ?)
    for i in range(rows):
        for j in range(cols):
            try:
                x = int(ms.gameboard[i][j])
                # print(x)
                #check if # of ?+x neighbors == x
                q = [] # queue of ?'s to flag
                bombs = 0 # count of neighboring flagged bombs
                # Now, check thy neighbors
                for ii in range(max(0,i-1),min(rows,i+2)):
                        for jj in range(max(0,j-1),min(cols,j+2)):
                            if (ii==i and jj==j):
                                continue
                            if(ms.gameboard[ii][jj]=='?'):
                                q.append((ii,jj))
                            if(ms.gameboard[ii][jj]=='x'):
                                bombs+=1
                if(len(q)+bombs == x):
                    for ij in q:
                        ms.flag(ij[0],ij[1])
                        found=True
                elif(bombs==x):
                    for ij in q:
                        ms.test(ij[0],ij[1])
                        found=True
                
            except:
                pass
    #last resort, just randomly select
    gameover = not any("?" in c for c in ms.gameboard)
    if(gameover):
        continue
    if not found:
        
        testi,testj=random.randint(0,9),random.randint(0,9)
        
        while(ms.gameboard[testi][testj] != "?"):
            testi,testj=random.randint(0,9),random.randint(0,9)
    
        gameover = ms.test(testi,testj)
    
won = not any("?" in c for c in ms.gameboard) and not any("o" in c for c in ms.gameboard)
ms.print_gameboard()
print("Win:",won)