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

    def __init__(self, deep,n,pa,x = 0,y = 0):
        self.Owner = None
        self.Status = False
        self.Size = n
        self.Depth = deep
        self.board = []
        self.Parent = pa
        self.x = x
        self.y = y
        
        if(self.Depth>1):
            for i in range(n):
                temp_list = []
                for j in range(n):
                    temp_list.append(Board(deep-1,n,self,i,j))
                self.board.append(temp_list)
                
        else:
            for i in range(n):
                temp_list = []
                for j in range(n):
                    temp_list.append(Item(self))
                self.board.append(temp_list)

            
    def check(self,x = 11,y = 11):
        if(x == 11 or y == 11):
            if(self.Status):
                return self.Owner
            else:
                return None
        else:
            if(self.board[x][y].isboard()==True):
                return self.board[x][y].Status
            else:
                return self.board[x][y].check()
        
    def complete(self, played_position: Coordinate):
        col = True
        line = True
        diag = True
        
        x, y = played_position.getAbscissa(), played_position.getOrdinate()
        selected = self.check(x,y)
        for i in range(self.Size):
            if(col and (self.check(i,y) != selected)):
                col = False
            if(line and (self.check(x,i) != selected)):
                line = False
                
        if(x == y or x == self.Size-1-y):
            diag1 = True
            diag2 = True
            for i in range(self.Size):
                if(diag1 and self.check(i,i) != selected):
                    diag1 = False
                if(diag2 and self.check(i, self.Size-1-i) != selected):
                    diag2 = False
            if(not(diag1 or diag2)):
                diag = False
        else:
             diag = False
        complete = False
        if(col or line or diag):
            self.Status = True
            self.Owner = selected
            complete = True
        else:
            complete =self.tie(selected)
        if(complete):
            if(self.Parent == None):
                print('Acabou')
            else:
                self.Parent.complete(Coordinate(self.x,self.y))
        else:
            return False
            
    def isboard(self):
        return self.Depth>0

    def tie(self,selected):
        complete = True
        x = 0
        o = 0
        if(self.board[0][0].isboard()):
            for i in range(self.Size):
                for j in range(self.Size):
                    temp = self.check(i,j)
                    if(temp == 'X'):
                        x += 1
                    elif(temp == 'O'):
                        o += 1
                    else:
                        return False
        else:
            for i in range(self.Size):
                for j in range(self.Size):
                    temp = self.board[i][j].check()
                    if(temp == 'X'):
                        x += 1
                    elif(temp == 'O'):
                        o += 1
                    else:
                        return False
                        
        if(x > o):
            self.Owner = 'X'
        elif(o > x):
            self.Owner = 'O'
        else:
            self.Owner = selected
        self.Status = True
        self.Depth = 0
        return True

    def owning(self,x,y,player):
        self.board[x][y].Status = True
        self.board[x][y].Owner = player

    def owning(self, player):
        self.Status = True
        self.Owner = player

    def choose(self, x,y,player):
        if(self.Depth>1):
            pass
        else:
            self.board[x][y].choose(player)
            self.complete(Coordinate(x,y))
            
    def peek(self, x,y):
        if(self.Depth):
            return self.board[x][y]
        else:
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
