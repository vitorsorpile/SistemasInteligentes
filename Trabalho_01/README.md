# Implementação BFS e DFS

# Contribuintes
Paulo Henrique Kubiack Gorla (19102059) & Vitor Sorpile Geraldo (19102063)

# Pré-requisitos
A versão utilizada do Python para a execução desse trabalho foi a 3.8.10 e as bibliotecas necessárias estão no arquivo requirements.txt.

# Execução
Com o terminal no diretório "Trabalho_01", o programa pode ser executado por meio do comando:
```python
python src/main.py
```
ou, dependendo da instalação, 
```python
python3 src/main.py
```

Na interface, é possível escolher um labirinto a ser resolvido clicando no botão "SELECT MAZE", caso não seja escolhido um, o labirinto no arquivo "lab00.txt" no diretório "labirintos" será utilizado. E a escolha de método de resolução, BFS ou DFS, é feita clicando nos respectivos botões da interface.
É assumido que a posição inicial, entrada do labirinto (representada pelo número 2), se localiza na posição (0, 0) e que existe um caminho possível até o objetivo, a saída do labirinto (representada pelo número 3).

# Informações
A função sucessor foi implementada com o nome "calculatePossibleSteps" na classe MazeSolver e passada por herança para as classes BFS e DFS.
Da mesma forma, a função de teste de objetivo foi implementada com o nome "isExit" na classe MazeSolver e herdada pelas classes BFS e DFS.
