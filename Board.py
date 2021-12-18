from colored import fg, style
import math

class Item():

    def isBoard():
        return isBoard

    def choose(Player_Code:str,Player_Color:int):
        self.Owner = Player_Code
        self.State = True
        self.color = Player_Color
        
    
    def check():
        if(self.State):
            return self.Owner
        else:
            return None
            
    def __init__():
        self.State = False
        self.Owner = None
        self.isBoard = False
                
    def __str__():
        if(self.State):
            return self.Owner
        else:
            return " " 
    


class Board(Item):

    def __init__(deep,n,pa):
        self.Owner = None
        self.Status = False
        self.Size = n
        self.Depth = deep
        self.board = [[]]
        self.Parent = pa
        self.isBoard = True
        
        if(Depth):
            for i in range(n):
                for j in range(n):
                    self.board[i][j] = Board(deep-1,n,self)
        else:
            for i in range(n):
                for j in range(n):
                    self.board[i][j] = Item()
                    

    def print_board():
        if(self.isComplete()):
            print("+-+")
            print("|"+
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
                    board[x][y].print_next_board(depth-1,i)
            print("+")
        else:
            for j in range(self.size*2):
                if(j%2 == 0):
                    print("|", end = '')
                else:
                    y += 1
                    if(depth==2):
                        board[x][y].print_next_board(depth-1,i)
                    else:
                        print(board[x][y]
            print("|")

        

    def print_next_board(index):
        if(depth == 0): print(fg(21)+"X"+fg(196),end = '')
        else:
            print(fg(196), end = '')
            if(index%2 == 0):
                for i in range(size*2-1):
                    if(i%2==0):
                        print("-", end = '')
                    else:
                        print("+", end = '')
                else:
                    for i in range(size*2-1):
                        if(i%2 == 0):
                            line(size,depth-1,index)
                        else:
                            print("|", end = '')
                            print(style.RESET, end = '')
                            
            
    def check():
        if(self.State or self.complete()):
            return self.Owner
        else:
            return None
        

    def complete(self, x, y):
        col = True
        line = True
        selected = board[x][j].check()
        for i in range(size):
            if(col and board[i][y].check() != selected):
                col = False
            if(line and board[x][i].check() != selected):
                line = False
        if(x == y):
            diag = True
            for i in range(size):
                if(diag and board[i][i].check() != selected):
                    diag = False
            if(diag):
                return True
        
        if(x == size-1-y):
            diag = True
            for i in range(size):
                if(diag and board[i][size-1-i].check() != selected):
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

    def tie():
        for i in range(self.size):
            for j in range(self.size):
                if(self.board[i][j].check()==None):
                    return False
        return True
                              
    def choose(x,y,player):
        if(Depth):
            print("Esse eh um tabuleiro externo, nao pode selecionar")
        else:
            board[x][y].choose(player)
            
    def peek(x,y):
        if(Depth):
            return board[x][y]
        else:
            print("Nao eh um tabuleiro!")
            return self
            
    def go_back():
        if(parent != None):
            return parent
        else:
            print("Este eh o tabuleiro mais externo!")
            return self

    def getSize():
        return Size
    
            
if __name__ == "__main__":
