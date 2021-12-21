
import pygame
from sys import exit
from Player import *
import Board
from Player import HumanPlayer

def win():
    pass

def create_settings(number,player,size):
    width = size[0]
    height = size[1]
    right_arrow = pygame.image.load('./images/arrow_right.png')
    right_arrow = pygame.transform.scale(right_arrow,(height/15,height/15))
    left_arrow = pygame.image.load('./images/arrow_left.png')
    left_arrow = pygame.transform.scale(left_arrow,(height/15,height/15))
    
    surface = pygame.Surface((width/6,height/15))
    surface.fill((100,100,100))
    surface.blit(left_arrow,(0,0))
    surface.blit(right_arrow,(width/6-height/15,0))
    font = pygame.font.Font(None,40)
    if(player):
        if(number == 0):
            surface.blit(font.render("Human",False,(255,255,255)),(width*1/18,height/45))
        elif(number == 1):
            surface.blit(font.render("Clumsy",False,(255,255,255)),(width*1/18,height/45))
        elif(number == 2):
            surface.blit(font.render("RawEater",False,(255,255,255)),(width*1/18,height/45))
    else:
        surface.blit(font.render(str(number),False,(255,255,255)),(width*3/36,height/45))
    return surface

def open_game_settings(screen,clock,deep,board_size,player1,player2):
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.Font(None,40)
    #Settings panel
    settings_Surface = pygame.Surface((width/5,height))
    settings_Surface.fill((150,150,150))
    deep_Surface = create_settings(deep,False,(width,height))
    deep_Text = font.render('Depth of the board',False,(255,255,255))

    size_Surface = create_settings(board_size,False,(width,height))
    size_Text = font.render('Size of the board',False,(255,255,255))

    player1_Surface = create_settings(player1,True,(width,height))
    player1_Text = font.render('Player 1 type',False,(255,255,255))

    player2_Surface = create_settings(player2,True,(width,height))
    player2_Text = font.render('Player 2 type',False,(255,255,255))
    
    right_arrow = pygame.image.load('./images/arrow_right.png')
    right_arrow = pygame.transform.scale(right_arrow,(height/15,height/15))
    left_arrow = pygame.image.load('./images/arrow_left.png')
    left_arrow = pygame.transform.scale(left_arrow,(height/15,height/15))

    left_rect = []
    left_rect.append(left_arrow.get_rect(topleft = (49*width/60,3/8*height)))
    left_rect.append(left_arrow.get_rect(topleft = (49*width/60,4/8*height)))
    left_rect.append(left_arrow.get_rect(topleft = (49*width/60,5/8*height)))
    left_rect.append(left_arrow.get_rect(topleft = (49*width/60,6/8*height)))

    right_rect = []
    right_rect.append(right_arrow.get_rect(topleft = (29*width/30,3/8*height)))
    right_rect.append(right_arrow.get_rect(topleft = (29*width/30,4/8*height)))
    right_rect.append(right_arrow.get_rect(topleft = (29*width/30,5/8*height)))
    right_rect.append(right_arrow.get_rect(topleft = (29*width/30,6/8*height)))
    
    deep_Surface.blit(left_arrow,(0,0))
    deep_Surface.blit(right_arrow,(width/6-height/15,0))

    size_Surface.blit(left_arrow,(0,0))
    size_Surface.blit(right_arrow,(width/6-height/15,0))

    player1_Surface.blit(left_arrow,(0,0))
    player1_Surface.blit(right_arrow,(width/6-height/15,0))

    player2_Surface.blit(left_arrow,(0,0))
    player2_Surface.blit(right_arrow,(width/6-height/15,0))

    settings_Surface.blit(left_arrow,(0,0))
    exit_rect = left_arrow.get_rect(topleft = (4/5*width,0))
    
    settings_Surface.blit(deep_Surface,(1*width/60,3/8*height))
    settings_Surface.blit(deep_Text,(1*width/30,22/64*height))
    
    settings_Surface.blit(size_Surface,(1*width/60,4/8*height))
    settings_Surface.blit(size_Text,(1*width/30,30/64*height))
    
    settings_Surface.blit(player1_Surface,(1*width/60,5/8*height))
    settings_Surface.blit(player1_Text,(1*width/30,38/64*height))
    
    settings_Surface.blit(player2_Surface,(1*width/60,6/8*height))
    settings_Surface.blit(player2_Text,(1*width/30,46/64*height))
    screen.blit(settings_Surface,(4*width/5,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = event.pos
                for i in range(4):
                    if(left_rect[i].collidepoint(mouse)):
                        if(i == 0 and deep > 1):
                            deep -= 1
                            deep_Surface = create_settings(deep,False,(width,height))
                            settings_Surface.blit(deep_Surface,(1*width/60,3/8*height))
                        elif(i == 1 and board_size > 0):
                            board_size -= 1
                            size_Surface = create_settings(board_size,False,(width,height))
                            settings_Surface.blit(size_Surface,(1*width/60,4/8*height))
                        elif(i == 2 and player1 > 0):
                            player1 -= 1
                            player1_Surface = create_settings(player1,True,(width,height))
                            settings_Surface.blit(player1_Surface,(1*width/60,5/8*height))
                        elif(i == 3 and player2 > 0):
                            player2 -= 1
                            player2_Surface = create_settings(player2,True,(width,height))
                            settings_Surface.blit(player2_Surface,(1*width/60,6/8*height))
                        break
                    elif(right_rect[i].collidepoint(mouse)):
                        if(i == 0 and deep < 5):
                            deep += 1
                            deep_Surface = create_settings(deep,False,(width,height))
                            settings_Surface.blit(deep_Surface,(1*width/60,3/8*height))
                        elif(i == 1 and board_size < 10):
                            board_size += 1
                            size_Surface = create_settings(board_size,False,(width,height))
                            settings_Surface.blit(size_Surface,(1*width/60,4/8*height))
                        elif(i == 2 and player1 < 2):
                            player1 += 1
                            player1_Surface = create_settings(player1,True,(width,height))
                            settings_Surface.blit(player1_Surface,(1*width/60,5/8*height))
                        elif(i == 3 and player2 < 2):
                            player2 += 1
                            player2_Surface = create_settings(player2,True,(width,height))
                            settings_Surface.blit(player2_Surface,(1*width/60,6/8*height))
                        break
                screen.blit(settings_Surface,(4/5*width,0))
                if(exit_rect.collidepoint(mouse)):
                    settings_Surface.fill((255,255,255))
                    screen.blit(settings_Surface,(4/5*width,0))
                    return (deep,board_size,player1,player2)
        clock.tick(60)
        pygame.display.update()
                

def refresh_board(screen,board):
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
    Mini_Board_Rect = []
    Item_Rect = []

    for i in range(size):
        temp_Board = []
        temp_Item1 = []
        for j in range(size):
            
            board = board.peek(i,j)
            if(board.Depth>0):
                temp_Item2 = []
                for k in range(size):
                    temp_Item3 = []
                    for l in range(size):
                        board = board.peek(k,l)
                        Item_Surface = None
                        if(board.isboard()):
                            Item_Surface = pygame.image.load('./images/#.xcf')
                        else:
                            player_item = board.check()
                            if(player_item == None):
                                Item_Surface = pygame.Surface((100,100))
                                Item_Surface.fill((255,255,255))
                            elif(player_item == 'X'):
                                Item_Surface = pygame.image.load('./images/X.xcf')
                            else:
                                Item_Surface = pygame.image.load('./images/O.xcf')
                        Item_Surface = pygame.transform.scale(Item_Surface,(widthMB*92/(size*100),widthMB*92/(100*size)))
                        temp_Item3.append(Item_Surface.get_rect(topleft = (width/6+(2/3)*height*(i/size+1/75)+widthMB/size*(k+0.04),height/6+(2/3)*height*(j/size+1/75)+widthMB/size*(l+0.04))))
                        Mini_Board_Surface.blit(Item_Surface,(widthMB/size*(k+0.04),widthMB/size*(l+0.04)))
                        board = board.go_back()
                    temp_Item2.append(temp_Item3)
                temp_Item1.append(temp_Item2)
            else:

                player_item = board.check()
                if(player_item == None):
                    Mini_Board_Surface = pygame.Surface((widthMB,widthMB))
                    Mini_Board_Surface.fill((255,255,255))
                elif(player_item == 'X'):
                    Mini_Board_Surface = pygame.image.load('./images/X.xcf')
                else:
                    Mini_Board_Surface = pygame.image.load('./images/O.xcf')
                Mini_Board_Surface = pygame.transform.scale(Mini_Board_Surface,(widthMB,widthMB))
                temp_Item1.append(Mini_Board_Surface.get_rect(topleft = (width/6+(2/3)*height*(i/size+1/75),height/6+(2/3)*height*(j/size+1/75))))
                
            Board_Surface.blit(Mini_Board_Surface,((2/3)*height*(i/size+1/75),(2/3)*height*(j/size+1/75)))
            board = board.go_back()
            
            temp_Board.append(Mini_Board_Surface.get_rect(topleft = (width/6+(2/3)*height*(i/size+1/75),height/6+(2/3)*height*(j/size+1/75))))        
        Item_Rect.append(temp_Item1)
        Mini_Board_Rect.append(temp_Board)
       
    screen.blit(Board_Surface,(width/6,height/6))
    
    return (Item_Rect,Mini_Board_Rect)

def play_game(screen,clock,board):

    size = board.getSize()

    Rect = refresh_board(screen,board)

    Item_Rect = Rect[0]
    Mini_Board_Rect = Rect[1]

    # Modificar com o nome do método:
    players = [HumanPlayer("X"), HumanPlayer("O")]
    
    turn = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                key = event.button
                mouse = event.pos
                if(key == 1):
                    if(len(Item_Rect) == 0):
                        pass
                    else:
                        for i in range(size):
                            for j in range(size):
                                if(board.check(i,j) == None and Item_Rect[i][j].collidepoint(mouse)):
                                    # Modificar aqui
                                    turn = 1 - turn
                                    board.choose(i,j,players[turn].getCharacter())
                                    if(board.complete(i,j)):
                                        win()
                                    refresh_board(screen,board)
                                else:
                                    for k in range(size):
                                        for l in range(size):
                                            if(board.Depth==2 and Item_Rect[i][j][k][l].collidepoint(mouse)):
                                                board = board.peek(i,j)
                                                if(board.check(k,l)==None):
                                                    turn = 1 - turn
                                                    board.choose(k,l, players[turn].getCharacter())
                                                if(board.complete(k,l)):
                                                    win()
                                                board = board.go_back()
                                                refresh_board(screen,board)
                elif(key == 3):
                    if(len(Mini_Board_Rect)==0):
                        pass
                    else:
                        for i in range(size):
                            for j in range(size):
                                if(board.Depth>1 and Mini_Board_Rect[i][j].collidepoint(mouse)):
                                    board = board.peek(i,j)
                                    Rect = refresh_board(screen,board)
                                    Item_Rect = Rect[0]
                                    Mini_Board_Rect = Rect[1]
                                    break
                            else:
                                continue
                            break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board = board.go_back()
                    Rect = refresh_board(screen,board)
                    Item_Rect = Rect[0]
                    Mini_Board_Rect = Rect[1]
                                    
                
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

    deep = 2
    board_size = 3
    player1 = 0
    player2 = 0

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if (event.type == pygame.MOUSEBUTTONUP):
                if(rect_Start.collidepoint(mouse)):
                    screen.fill((255,255,255))
                    board = Board.Board(deep,board_size,None)   
                    play_game(screen,clock,board)
                    return
                elif(rect_Options.collidepoint(mouse)):
                    pass
                elif(rect_Exit.collidepoint(mouse)):
                    pygame.quit()
                    exit()
                elif(rect_Config.collidepoint(mouse)):
                    settings = open_game_settings(screen,clock,deep,board_size,player1,player2)
                    deep = settings[0]
                    board_size = settings[1]
                    player1 = settings[2]
                    player2 = settings[3]

        
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
