from colored import fg, style
from AuxiliarTypes import Coordinate
import math

class Item():

    def __init__(self):
        self.State = False
        self.Owner = None
        self.isBoard = False

    def isboard(self):
        return self.isBoard

    def choose(self, Player_Code:str,Player_Color:int):
        self.Owner = Player_Code
        self.State = True
        self.color = Player_Color
        
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

class Board(Item):

    def __init__(self, deep,n,pa):
        self.Owner = None
        self.Status = False
        self.Size = n
        self.Depth = deep
        self.board = [[]]
        self.Parent = pa
        self.isBoard = True
        
        if(self.Depth):
            for i in range(n):
                for j in range(n):
                    self.self.board[i][j] = self.board(deep-1,n,self)
        else:
            for i in range(n):
                for j in range(n):
                    self.self.board[i][j] = Item()
                    

    def printBoard(self):
        if(self.isComplete()):
            print("+-+")
            print("|")
        if(self.Depth > 2): depth = 2
        else: depth = self.Depth
       
        x = -1
        y = 0
        for i in range(self.size**depth*2+1):
            if(i%(self.size*depth) == 0):
                print(("+"+"-")*(self.size**depth)+"+")
                x += 1
                y = 0
            elif(i%2==0):
                for j in range(self.size*2):
                    if(j%2 == 0):
                        print("+", end = '')
                    else:
                        self.board[x][y].print_next_self.board(depth-1,i)
                print("+")
            else:
                for j in range(self.size*2):
                    if(j%2 == 0):
                        print("|", end = '')
                    else:
                        y += 1
                        if(depth==2):
                            self.board[x][y].print_next_board(depth-1,i)
                        else:
                            print(self.board[x][y])
                print("|")

    def print_next_board(self, index):
        if(self.Depth == 0): print(fg(21)+"X"+fg(196),end = '')
        else:
            print(fg(196), end = '')
            if(index%2 == 0):
                for i in range(self.Size*2-1):
                    if(i%2==0):
                        print("-", end = '')
                    else:
                        print("+", end = '')
                else:
                    for i in range(self.Size*2-1):
                        if(i%2 == 0):
                            line(self.Size,self.Depth-1,index)
                        else:
                            print("|", end = '')
                            print(style.RESET, end = '')
                            
            
    def check(self):
        if(self.State or self.complete()):
            return self.Owner
        else:
            return None
        

    def complete(self, x, y):
        col = True
        line = True
        selected = self.self.board[x][j].check()
        for i in range(self.size):
            if(col and self.self.board[i][y].check() != selected):
                col = False
            if(line and self.self.board[x][i].check() != selected):
                line = False
        if(x == y):
            diag = True
            for i in range(self.Size):
                if(diag and self.board[i][i].check() != selected):
                    diag = False
            if(diag):
                return True
        
        if(x == self.Size-1-y):
            diag = True
            for i in range(self.Size):
                if(diag and self.board[i][self.Size-1-i].check() != selected):
                    diag = False
            if(diag):
                self.State = True
                self.Owner = selected.check()
                return True
        if(col or line):
            self.State = True
            self.Owner = selected.check()
            return True
        else:
            return self.tie()

    def tie(self):
        for i in range(self.size):
            for j in range(self.size):
                if(self.self.board[i][j].check()==None):
                    return False
        return True
                              
    def choose(self, x,y,player):
        if(self.Depth):
            print("Esse eh um tabuleiro externo, nao pode selecionar")
        else:
            self.board[x][y].choose(player)
            
    def peek(self, x,y):
        if(self.Depth):
            return self.board[x][y]
        else:
            print("Nao eh um tabuleiro!")
            return self
    
    def peek(self,coord: Coordinate):
        if(self.Depth):
            return self.board[coord.getAbscissa()][coord.getOrdinate()]
        else:
            print("Nao eh um tabuleiro!")
            return self

    def go_back(self):
        if(self.parent != None):
            return self.parent
        else:
            print("Este eh o tabuleiro mais externo!")
            return self

    def getSize(self):
        return self.Size
    
# if __name__ == "__main__":
