import pygame
from sys import exit
#from Player import *
import Board

def win():
    pass

def open_game_settings(screen,clock):
    pass


def play_game(screen,clock,board):
    #Create screen and board variables
    width = screen.get_width()
    height = screen.get_height()
    size = board.getSize()
    widthMB = (46/(75*size))*height
    
    #Create Board
    Board_Surface = pygame.Surface((2/3*height,2/3*height))
    Board_Surface.fill((0,0,0))
    Mini_Board_Surface = pygame.Surface((widthMB,widthMB))
    Mini_Board_Surface.fill((150,0,205))

    
    for i in range(size):
        for j in range(size):
            board = board.peek(i,j)
            if(board.isboard()):
                for k in range(size):
                    for l in range(size):
                        board = board.peek(k,l)
                        Item_Surface = None
                        if(board.isboard()):
                            Item_Surface = pygame.image.load('./images/#.xcf')
                        else:
                            player_item = board.check(k,l)
                            if(player_item == None):
                                Item_Surface = pygame.Surface((100,100))
                                Item_Surface.fill((255,255,255))
                            elif(player_item == 'X'):
                                Item_Surface = pygame.image.load('./images/X.xcf')
                            else:
                                Item_Surface = pygame.image.load('./images/O.xcf')
                        Item_Surface = pygame.transform.scale(Item_Surface,(widthMB*92/(size*100),widthMB*92/(100*size)))
                        Mini_Board_Surface.blit(Item_Surface,(widthMB/size*(k+0.04),widthMB/size*(l+0.04)))
                        board = board.go_back()
            else:
                player_item = board.check(i,j)
                if(player_item == None):
                    Mini_Board_Surface = pygame.Surface((widthMB,widthMB))
                    Mini_Board_Surface.fill((255,255,255))
                elif(player_item == 'X'):
                    Mini_Board_Surface = pygame.image.load('./images/X.xcf')
                else:
                    Mini_Board_Surface = pygame.image.load('./images/O.xcf')
            Board_Surface.blit(Mini_Board_Surface,((2/3)*height*(i/size+1/75),(2/3)*height*(j/size+1/75)))
            board = board.go_back()
                                
                                
    screen.blit(Board_Surface,(width/6,height/6))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if(board.check != None):
            win()
        clock.tick(60)
        pygame.display.update()

def title_screen(screen,clock):
    #Get the Screen's size
    height = screen.get_height()
    width = screen.get_width()

    #Setup font
    Font = pygame.font.Font(None,60)

    
    #Create the elements of the screen
    #Title
    title_surface = pygame.image.load('./images/Titulo.png')

    #Start game Button
    button_Start = pygame.Surface((width/6,height/15))
    button_Start.fill((50,50,50))
    inner_Start = pygame.Surface((98*width/600,height/15-1/300*width))
    inner_Start.fill((100,100,100))
    text_Start = Font.render('START GAME', False,(255,255,255))
    inner_Start.blit(text_Start,(inner_Start.get_width()/15,inner_Start.get_height()/2-15))
    button_Start.blit(inner_Start,(1/600*width,1/600*width))
    rect_Start = button_Start.get_rect(topleft=(width*5/12,height*5/10))

    #Options Button
    button_Options = pygame.Surface((width/6,height/15))
    button_Options.fill((50,50,50))
    inner_Options = pygame.Surface((98*width/600,height/15-1/300*width))
    inner_Options.fill((100,100,100))
    text_Options = Font.render('OPTIONS', False,(255,255,255))
    inner_Options.blit(text_Options,(inner_Options.get_width()*2/11,inner_Options.get_height()/2-15))
    button_Options.blit(inner_Options,(1/600*width,1/600*width))
    rect_Options = button_Options.get_rect(topleft = (width*5/12,height*7/10))

    #Exit game Button
    button_Exit = pygame.Surface((width/6,height/15))
    button_Exit.fill((50,50,50))
    inner_Exit = pygame.Surface((98*width/600,height/15-1/300*width))
    inner_Exit.fill((100,100,100))
    text_Exit = Font.render('EXIT GAME', False,(255,255,255))
    inner_Exit.blit(text_Exit,(inner_Exit.get_width()/8,inner_Exit.get_height()/2-15))
    button_Exit.blit(inner_Exit,(1/600*width,1/600*width))
    rect_Exit = button_Options.get_rect(topleft = (width*5/12,height*8/10))

    #Configuration Button
    button_Config = pygame.Surface((width/6,height/15))
    button_Config.fill((50,50,50))
    inner_Config = pygame.Surface((width/6-1/300*width,height/15-1/300*width))
    inner_Config.fill((100,100,100))
    text_Config = Font.render('SETUP GAME', False,(255,255,255))
    rect_Config = button_Config.get_rect(topleft = (width*5/12,height*6/10))
    inner_Config.blit(text_Config,(inner_Config.get_width()/15,inner_Config.get_height()/2-15))
    button_Config.blit(inner_Config,(1/600*width,1/600*width))

    
    #Put the elements on the Screen
    screen.blit(title_surface,(width/2-440,0))
    screen.blit(button_Start,rect_Start)
    screen.blit(button_Options,rect_Options)
    screen.blit(button_Exit,rect_Exit)
    screen.blit(button_Config,rect_Config)


     



    
    
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if (event.type == pygame.MOUSEBUTTONUP):
                if(rect_Start.collidepoint(mouse)):
                    screen.fill((255,255,255))
                    board = Board.Board(1,5,None)   
                    play_game(screen,clock,board)
                    return
                elif(rect_Options.collidepoint(mouse)):
                    pass
                elif(rect_Exit.collidepoint(mouse)):
                    pygame.quit()
                    exit()
                elif(rect_Config.collidepoint(mouse)):
                    open_game_settings(screen,clock)

        
        clock.tick(60)
        pygame.display.update()



        
    



def main():
    #Initialize Pygame     
    pygame.init()
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.set_caption('Mega Jogo da Velha')
    clock = pygame.time.Clock()


    #Set the parameters for the creation of the game's screens
    screen.fill('White')
    option = 0
    while True:
        title_screen(screen,clock)

    
    """moves = ["X","O"]
    print("Bem vindo ao Mega jogo da velha!\nInicialmente, configure o jogo.")
    valid_input = False
    print()
    print("1º) Defina quais serão os jogadores.\n    1. Jogador Humano, 2. Jogador Estabanado, 3. Jogador Come-crú\n    Caso não saiba, escreva 'help' ao lado de \">\" e pressione Enter")
    while (not valid_input):
        _input = input("> ").strip()
        if (_input == "help"):
            print("== help ==")
            print("Para se definir os jogadores, escreva dois números separados do outro, de modo que cada número se relaciona com um dos jogadores.")
            print("Lembre-se: os jogadores são: 1. Jogador Humano, 2. Jogador Estabanado, 3. Jogador Come-crú.")
            print("Exemplo: A fim de se selecionar um Jogador Humano e um Come-Crú, você deverá escrever, ao lado de \">\", 1 3")
            print("==========")
            continue
        _input = _input.split()
        if (len(_input) != 2):
            print(f"Número de argumentos inválido! Esperava-se 2, mas se recebeu {len(_input)}"); continue
        if (_input[0] not in {"1","2","3","4"}):
            print(f"Primeiro jogador inválido! Esperava-se um número entre 1 e 4, mas se recebeu {_input[0]}"); continue
        if (_input[1] not in {"1","2","3","4"}):
            print(f"Segundo jogador inválido! Esperava-se um número entre 1 e 4, mas se recebeu {_input[1]}"); continue
        _input = [int(x) for x in _input]
        valid_input = True
    
    print("Jogadores Selecionados: ")
    players = []
    _players = "    "
    for i in {0,1}:
        if (_input[i] == 1):
            _players = _players + f"{i+1}º) Jogador Humano ({moves[i]});\n    "; players.append(HumanPlayer(moves[i]))
        elif (_input[i] == 2):
            _players = _players + f"{i+1}º) Jogador Estabanado ({moves[i]});\n    "; players.append(ClumsyPlayer(moves[i]))
        elif (_input[i] == 3):
            _players = _players + f"{i+1}º) Jogador Come-crú ({moves[i]});\n    "; players.append(RawEaterPlayer(moves[i]))
        else:
            _players = _players + f"{i+1}º) Jogador IA-Fácil ({moves[i]});\n    "
    print(_players)
    print(players)
    turn = 0
    while(not board.isComplete()):
        macroCell_coord = players[turn].play()
        # Implementar overload de peek() para receber Coordinate
        if (board.peek(macroCell_coord).isComplete()):
            # Método para checar se alguém ganho e mudar o estado da board.peek()
            pass
        turn = 1 - turn"""

if __name__ == "__main__":
    main()
