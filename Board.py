from colored import fg, style
from AuxiliarTypes import Coordinate
import pytest

class Item():

    def __init__(self,parent):
        self.State = False
        self.Owner = None
        self.Parent = parent
        self.Depth = 0

    def isboard(self):
        return False

    def choose(self, Player_Code:str):
        self.Owner = Player_Code
        self.State = True
        
    def check(self):
        if(self.State):
            return self.Owner
        else:
            return None
                
    def __str__(self):
        if(self.State):
            return self.Owner
        else:
            return " "

    def go_back(self):
        return self.Parent

class Board(Item):

    def __init__(self, deep,n,pa):
        self.Owner = None
        self.Status = False
        self.Size = n
        self.Depth = deep
        self.board = []
        self.Parent = pa
        
        if(self.Depth>1):
            for i in range(n):
                temp_list = []
                for j in range(n):
                    temp_list.append(Board(deep-1,n,self))
                self.board.append(temp_list)
                
        else:
            for i in range(n):
                temp_list = []
                for j in range(n):
                    temp_list.append(Item(self))
                self.board.append(temp_list)

            
    def check(self,x,y):
        if(self.board[x][y].isboard()==True):
            return self.board[x][y].Status
        else:
            return self.board[x][y].check()
        
    def complete(self, played_position: Coordinate):
        col = True
        line = True
        
        x, y = played_position.getAbscissa(), played_position.getOrdinate()
        selected = self.check(x,y)
        # print(selected)
        for i in range(self.Size):

            if(col and self.check(i,y) != selected):
                col = False
            if(line and self.check(x,i) != selected):
                line = False
        if(x == y):
            diag = True
            for i in range(self.Size):
                if(diag and self.check(i,i) != selected):
                    diag = False
            if(diag):
                # self.State = True
                # self.Owner = selected
                return True
        
        if(x == self.Size-1-y):
            diag = True
            for i in range(self.Size):
                if(diag and self.check(i, self.Size-1-i) != selected):
                    diag = False
            if(diag):
                self.State = True
                self.Owner = selected
                return True
        if(col or line):
            self.State = True
            self.Owner = selected
            return True
        # else:
        #     return self.tie()

    def isboard(self):
        return self.Depth>0

    def tie(self):
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if(self.check(i,j)==None):
        #             return False
        #         elif ()
        bools = [False, False, False, False]
        for i in range(self.Size):
            for j in range(1, self.Size):
                if self.check(i,j-1) != self.check(i,j):
                    bools[0] = True

        for j in range(self.Size):
            for i in range(1,self.Size):
                if self.check(i-1, j) != self.check(i,j):
                    bools[1] = True
        
        for k in range(1, self.Size):
            if self.check(k-1,k-1) != self.check(k,k):
                bools[2] = True

        for k in range(self.Size-1,1):
            if self.check(k+1,k+1) != self.check(k, self.Size - 1 - k):
                bools[3] = True

        return (True in bools)

    def owning(self,x,y,player):
        self.board[x][y].Status = True
        self.board[x][y].Owner = player

    def owning(self, player):
        self.Status = True
        self.Owner = player

    def choose(self, x,y,player):
        if(self.Depth>1):
            print("Esse eh um tabuleiro externo, nao pode selecionar")
        else:
            self.board[x][y].choose(player)
            
    def peek(self, x,y):
        if(self.Depth):
            return self.board[x][y]
        else:
            print("Nao eh um tabuleiro!")
            return self

    def go_back(self):
        if(self.Parent != None):
            return self.Parent
        else:
            # print("Este eh o tabuleiro mais externo!")
            return self

    def getSize(self):
        return self.Size
    
if __name__ == "__main__":
    board = Board(3,3,None)
    board = board.peek(0,0)
    board = board.peek(0,0)
    board = board.go_back()
