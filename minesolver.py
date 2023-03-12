from minesweeper import minesweeper
import random
# random.seed(1000158)

def minesolver(ms,rows,cols,difficulty):
    
    gameover=False
    while(not gameover):
        #First check for completion
        gameover = not any("?" in c for c in ms.gameboard)
        if(gameover):
            continue
        possibles = [[()]*cols for _ in range(rows)] 
        found=False
        #First, check for any obvious solutions (ie 1 with only 1 ?)
        for i in range(rows):
            for j in range(cols):
                try:
                    x = int(ms.gameboard[i][j])
                    
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
                    possibles[i][j] = (x-bombs,q)
                    
                except:
                    pass
        if(found):
            print("easy algorithm!")
        #Possible neighbors
        if not found:
            for i in range(rows):
                for j in range(cols):
                    if len(possibles[i][j]) > 0 and possibles[i][j][0]>0:
                    
                        for ii in range(max(0,i-2),min(rows,i+3)):
                            for jj in range(max(0,j-2),min(cols,j+3)):
                                if (ii==i and jj==j):
                                    continue
                                if len(possibles[ii][jj]) > 0 and possibles[ii][jj][0]>0:
                    
                                    if all(p in possibles[ii][jj][1] for p in possibles[i][j][1]):                                    
                                        leftover = set(possibles[ii][jj][1])-set(possibles[i][j][1])
                                        diff = possibles[ii][jj][0]-possibles[i][j][0]
                                        
                                        if(len(leftover)!=0):
                                            print(possibles[i][j]," | ",possibles[ii][jj],end=" --> ")
                                            print("possible algorithm: ",end='')
                                            print(diff,leftover)
                                            if(diff==0):
                                                found=True
                                                for p in leftover:
                                                    ms.test(p[0],p[1])
                                                
                                            elif(diff==len(leftover)):
                                                found=True
                                                for p in leftover:
                                                    ms.flag(p[0],p[1])
                                                
                                        
                                if found:
                                    break
                            if found:
                                break
                    if found:
                        break
                if found:
                    break
        #Now, prepare probability for random
        probabilities = [[1.0]*cols for _ in range(rows)]
        if not found:
            for i in range(rows):
                for j in range(cols):
                    if ms.gameboard[i][j] == "?":               
                        for ii in range(max(0,i-2),min(rows,i+3)):
                            for jj in range(max(0,j-2),min(cols,j+3)):
                                if (ii==i and jj==j):
                                    continue
                                if len(possibles[ii][jj]) > 0 and (i,j) in possibles[ii][jj][1]:
                                    if probabilities[i][j] == 1.0:
                                        probabilities[i][j] = 0
                                    
                                    chance=possibles[ii][jj][0]/len(possibles[ii][jj][1])
                                    
                                    probabilities[i][j] = 1 - ((1-probabilities[i][j]) * (1-chance))
                                    
                                    # print("probably ",i,j,chance,probabilities[i][j])
                                        
        #last resort, just randomly select
        gameover = not any("?" in c for c in ms.gameboard)
        if(gameover):
            continue
        if not found:
            guesslist = []
            for i in range(rows):
                for j in range(cols):
                    if ms.gameboard[i][j] == "?":
                        guesslist.append((i,j))
            
            best_guess = guesslist[0]
            for g in guesslist:
                if probabilities[g[0]][g[1]] < probabilities[best_guess[0]][best_guess[1]]:
                    best_guess = g
            
            # guess=random.choice(guesslist)
            # print("Random Guess: out of",len(guesslist),":",guess,"Probability of bomb =",probabilities[guess[0]][guess[1]])
            print("Best Guess:",best_guess,"Probability of bomb =",probabilities[best_guess[0]][best_guess[1]])
            # gameover = ms.test(guess[0],guess[1]) or not any("?" in c for c in ms.gameboard)
            gameover = ms.test(best_guess[0],best_guess[1]) or not any("?" in c for c in ms.gameboard)
        
    won = not any("?" in c for c in ms.gameboard) and not any("o" in c for c in ms.gameboard)
    ms.print_gameboard()
    print("Win:",won)