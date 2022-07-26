# Estudo dirigido sobre Redes Neurais Artificiais

# Contribuintes
Paulo Henrique Kubiack Gorla (19102059) & Vitor Sorpile Geraldo (19102063)

# Pré-requisitos
A versão utilizada do Python para a execução desse trabalho foi a 3.8.10 e as bibliotecas necessárias estão no arquivo requirements.txt.

# Execução
A execução dessa trabalho é dividida em duas etapas, logo existem dois scripts python. O primeiro, "main.py", é para treinamento das redes neurais e geração dos modelos, esse pode ser executado de forma a gerar os três modelos, cada um com uma topologia diferente, de uma vez só ou pode ser especificado qual modelo deve ser gerado por meio de um argumento de linha de comando:

Para gerar os três modelos use o comando:

```python
python main.py
```
E para gerar um modelo específico:

```python
python main.py {modelo}
```
Onde os valores aceitos para modelo são 1, 2 ou 3, que representam cada uma das topologias.

O segundo script, "guess_script.py", deve ser utilizado após a geração do modelo desejado por meio do script "main.py" e nele deve ser escolhido o modelo por um argumento de linha de comando, o qual será usado para inferir uma resposta, de acordo com os dados usados para treinamento, para os valores passados pela entrada padrão do sistema (console/cmd/terminal):

```python
python guess_script.py {modelo}
```
Onde os valores aceitos para modelo são 1, 2 ou 3, que representam cada uma das topologias. 
