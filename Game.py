
from Player import *

def main():
    
    # Precisa declarar uma board:
    # board = Board(3)

    moves = ["X","O"]
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
        turn = 1 - turn

if __name__ == "__main__":
    main()