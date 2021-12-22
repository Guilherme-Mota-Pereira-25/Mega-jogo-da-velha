from typing import Tuple
from AuxiliarTypes import Coordinate
import Board
from random import randint

class Player:

    def __init__(self,  character: str):
        self.character = character

    def play(self, board: Board) -> Coordinate:
        pass

    def getCharacter(self) -> str:
        return self.character

class HumanPlayer(Player):

    def __init__(self, character: str):
        super().__init__(character)
    
    def play(self, board: Board) -> bool:
        '''Função que requisita ao jogador uma jogada.'''

        sucessful_play = False
        M_i, M_j = 0, 0
        while not sucessful_play:
            _input = (int(x) for x in input().split())
            valid_input = True
            for i in _input: 
                if (not 0 <= i <= 2):
                    valid_input = False; break
            if (not valid_input): 
                print("Input não é válido! Tente novamente:")
                continue

            board.peek(_input[0], _input[1]).peek(_input[2], _input[3]).choose(self.character)
            sucessful_play = True
        return Coordinate(M_i, M_j)

class ClumsyPlayer(Player):    

    def __init__(self, character: str) -> None:
        super().__init__(character)

    def play(self, board: Board) -> Coordinate:
        successful_play = False
        M_i, M_j = 0, 0
        while not successful_play:
            M_i, M_j = randint(2), randint(2)
            if (not board.peek(M_i,M_j).check() == None):
                continue

            m_i, m_j = randint(2), randint(2)
            if (not board.peek(M_i, M_j).peek(m_i.m_j).check() == None):
                continue

            board.peek(M_i, M_j).peek(m_i.m_j).choose(self.character)
            successful_play = True
        return Coordinate(M_i, M_j)

class RawEaterPlayer(Player):

    def __init__(self, character: str) -> None:
        super().__init__(character)

    def play(self, board: Board) -> Coordinate:
        '''Função que joga conforme um jogador come-crú
        Assume-se que o tabuleiro ainda não está completo e que ainda há espaços em que se pode jogar
        
        Argumento:
        - board: Board (Tabuleiro [Será modificado na jogada] )
        Retorno:
        - Coordinate (Coordenada da célula do macro-tabuleiro em que o jogador jogou)'''
        pos_Macro = 0
        while not board.isValid(pos_Macro//3,pos_Macro%3): pos_Macro = pos_Macro+1
        pos_Macro_x, pos_Macro_y = pos_Macro//3, pos_Macro%3
        pos_micro = 0
        while pos_micro < 9 and not board.peek(pos_Macro_x,pos_Macro_y).peek(pos_micro//3, pos_micro%3): pos_micro = pos_micro+1
        if (pos_micro != 9):
            board.peek(pos_Macro_x,pos_Macro_y).peek(pos_micro//3,pos_micro%3).peek(self.character)
        return Coordinate(pos_Macro_x, pos_Macro_y)

class EasyAIPlayer(Player):
    
    def __init__(self, character: str):
        super().__init__(character)
    
    def play(self, board: Board) -> Coordinate:
        return super().play()