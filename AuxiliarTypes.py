class Coordinate:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    # Encapsulamento das propriedades
    def getAbscissa(self) -> int:
        "Retorna o valor da abscissa da Coordenada"
        return self.x
    def getOrdinate(self) -> int:
        "Retorna o valor da ordenada da Coordenada"
        return self.y
    
    def setAbscissa(self, new_x: int) -> None:
        "Coloca-se um novo valor para a abscissa da Coordenada"
        self.x = new_x

    def setOrdinate(self, new_y: int) -> None:
        "Coloca-se um novo valor para a abscissa da Coordenada"
        self.y = new_y