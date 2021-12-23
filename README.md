# Mega-jogo-da-velha

Repositório cujo fim é facilitar o progresso do desenvolvimento do 4º e último Exercício Programa da disciplina MAC0216/DCC/IME/USP.

Com exceção das imagens, todos os arquivos se encontram no mesmo diretório 

## Compilação

Para executar o jogo, execute:

`python3 Game.py`

## Excução

Ao abrir o jogo, uma tela se abrirá e você encontrará 3 botões, um dos quais funciona como o botão de saída: [Quit Game]. Assim, para jogar, clique nos seguintes botôes em conformidade com a sequência que se segue:

### [Setup Game]

Quando você clicar nesse botão, um menu lateral aparecerá a fim de selecionar, em ordem de cima para baixo:

**a) A profundidade do tabuleiro (Depth of the board):** Uma vez que foi buscado generealizar o código para tabuleiros de profundidade maior, poderá ser possível haver uma configuração de macrotabuleiro dentro de uma célula de outro tabuleiro. Exemplo: uma profundidade de 3 indica que cada que cada célula do tabuleiro conterá um macrotabuleiro, enquanto uma profundidade de 2 indica um macrotabuleiro normal.

**b) As dimensões do tabuleiro (Size of the board):** Quantas células cada tabuleiro terá: 3x3, 4x4, ...

**c) Jogador 1 (Player 1 type):** Que pode ser Humano (Human), Estabanado (Clumsy) ou Come-crú (Raw Eater).

**d) Jogador 2 (Player 2 type):** Semelhante ao Jogador 1.

_Atente-se:_ O Jogador 1 será o primeiro a jogar e jogará com **X**, enquanto o Jogador 2 jogará, assim, em segundo e com **O**.

### [Play Game]

No momento em que você clicar nesse botão, a board aparecerá. Com isso, você poderá:

**a) Clicar com o botão direito sobre uma célula:** Ao clicar, o jogo executará uma aproximação (popularmente conhecido como "zoom") para enxergar melhor um tabuleiro interno. Recomenda-se utilizar ess ferramente para tabuleiros com profundidade maior do que 2.

**b) Apertar espaço:** Esta ação desfazerá a ampliação feita por um botão direito, de modo a te levar ao tabuleiro superior em relação a uma célula.

**c) Clicar em uma célula:** Ao clicar em uma célula, o jogo colocará a marcação correspondente ao do jogador.

O jogo progredirá na medida em que os jogadores, quer humanos ou não, jogarem e, ao finalizar, o jogo congelará no tabuleiro cuja configuração é a do vencedor.
