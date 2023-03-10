import random
class minesweeper:
    def __init__(self,rows,cols,difficulty):
        self.minefield=[[False]*cols for _ in range(rows)]
        self.board = [[0]*cols for _ in range(rows)]
        self.gameboard = [["?"]*cols for _ in range(rows)]
        self.rows=rows
        self.cols=cols
        for i in range(rows):
            for j in range(cols):
                self.minefield[i][j] = random.random() < difficulty
                
                if(self.minefield[i][j]):
                    for ii in range(max(0,i-1),min(rows,i+2)):
                        for jj in range(max(0,j-1),min(cols,j+2)):
                            self.board[ii][jj]+=1
    
    def print_minefield(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.minefield[i][j]):
                    print("o ",end='')
                else:
                    print("  ",end='')
            print()
            
    def print_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.board[i][j],end=' ')
            print()
            
    def print_gameboard(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.gameboard[i][j],end=' ')
            print()
    
    #check if i,j has mine
    def test(self,i,j):
        if(self.minefield[i][j]):
            self.gameboard[i][j] = "o" # bomb
        else:
            neighbors=[]
            visited=set()
            if(self.board[i][j]==0):
                self.gameboard[i][j] = " "
                neighbors.append((i,j))
                visited.add((i,j))
            else:
                self.gameboard[i][j] = str(self.board[i][j])
            
            while(len(neighbors)>0):
                # print(neighbors)
                n = neighbors.pop(0)
                # print(n)
                for ii in range(max(0,n[0]-1),min(self.rows,n[0]+2)):
                        for jj in range(max(0,n[1]-1),min(self.cols,n[1]+2)):
                            if (ii==n[0] and jj==n[1]):
                                continue
                            # print(ii,jj)
                            if(self.gameboard[ii][jj]=="?" and (ii,jj) not in visited):
                                if(self.board[ii][jj]==0):
                                    self.gameboard[ii][jj] = " "
                                    neighbors.append((ii,jj))
                                    visited.add((ii,jj))
                                else:
                                    self.gameboard[ii][jj] = str(self.board[ii][jj])
            
        
                            
        return self.minefield[i][j]
        
    def flag(self,i,j):
        if self.gameboard[i][j] == '?':
            self.gameboard[i][j] = "x" # flag
        elif self.gameboard[i][j] == 'x':
            self.gameboard[i][j] = '?'
        else:
            print("Cannot flag a revealed space")
    