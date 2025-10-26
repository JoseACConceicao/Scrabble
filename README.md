# Scrabble

Este projeto é uma implementação em Python do clássico jogo de palavras Scrabble. O programa permite partidas de 2 a 4 jogadores, com suporte para jogadores humanos e agentes controlados pelo computador (BOT's) em diferentes níveis de dificuldade.

## Interface do Jogo

O jogo decorre numa interface de texto, que representa o tabuleiro de $15 \times 15$. As letras são colocadas no tabuleiro e a pontuação de cada jogador é atualizada a cada turno.

Exemplo de um tabuleiro a meio do jogo:

                           1 1 1 1 1 1
         1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
       +-------------------------------+
     1 | . . . . . . . . . . . . . . . | 
     2 | . . . . . P Y T H O N . . . . | 
     3 | . . . . . R . . . . . . . . . | 
     4 | . . . . . O . . . . . . . . . | 
     5 | . . . . . G . . . . . . . . . | 
     6 | . . S C R A B B L E . . . . . | 
     7 | . . . . . A . E . . . . . . . | 
     8 | . . . . . M . N . . . . . . . | 
     9 | . . . . . A . F . . . . . . . | 
    10 | . . . . . Ç . I . . . . . . . | 
    11 | . . . . . A . C . . . . . . . | 
    12 | . . . . . O . A . . . . . . . | 
    13 | . . . . . . . . . . . . . . . | 
    14 | . . . . . . . . . . . . . . . | 
    15 | . . . . . . . . . . . . . . . | 
       +-------------------------------+

## Regras Básicas

O objetivo do jogo é acumular mais pontos que os adversários. Os pontos são obtidos pela colocação de palavras no tabuleiro.

1.  **Configuração Inicial:** Cada jogador começa com 7 letras, retiradas aleatoriamente de um "saco".
2.  **Turno de Jogo:** Em cada turno, o jogador pode escolher uma de três ações:
    * **Passar:** Abdica da sua vez, não joga e recebe zero pontos.
    * **Trocar:** Devolve uma ou mais das suas letras ao saco e retira o mesmo número de novas letras.
      - Recebe zero pontos.
      - Esta ação só é válida se existirem pelo menos 7 letras no saco, no caso de um ***jogador agente***, ou se exixtirem letras suficientes no saco para substituir as letras que o ***jogador humano*** pretenda trocar.
    * **Jogar:** Coloca letras da sua mão no tabuleiro para formar uma palavra.

3.  **Regras de Colocação de Palavras:**
    * As palavras devem ser lidas da esquerda para a direita ou de cima para baixo. 
    * **Primeira Jogada:** A primeira palavra jogada na partida tem de ter pelo menos duas letras e deve obrigatoriamente cobrir a casa central (8,8).
    * **Jogadas Seguintes:** Qualquer palavra nova deve utilizar pelo menos uma letra já presente no tabuleiro, ligando-se às palavras existentes (como num jogo de palavras cruzadas).
    * Todas as letras jogadas num único turno devem ser colocadas numa única linha (horizontal ou vertical).
    * A palavra formada deve existir no vocabulário fornecido ao jogo. [cite: 10, 355]

4.  **Pontuação:**
    * Cada letra possui um valor de pontuação específico.
    * A pontuação de uma palavra é a soma dos pontos de todas as letras que a compõem.
    * Após jogar, o jogador retira do saco o mesmo número de letras que utilizou, repondo a sua mão para 7 letras (ou menos, se o saco estiver a ficar vazio).

5.  **Fim do Jogo:** O jogo termina numa de duas condições:
    * Um jogador joga a sua última letra e o saco de letras está vazio.
    * Todos os jogadores passam a vez de forma consecutiva.

O ***vencedor*** é o jogador com a pontuação total mais elevada no final do jogo.

## Como Jogar

O jogo é iniciado através da função `scrabble2`. Durante a partida, os jogadores interagem através de comandos específicos.

### Sintaxe das Jogadas (Jogadores Humanos)

Quando for a vez de um jogador humano, o programa exibirá uma mensagem como `Jogada (Nome_Jogador):`. O jogador deve então introduzir um dos seguintes comandos:

* **Passar:**
    ```
    P
    ```

* **Trocar Letras:**
    ```
    T <letra1> <letra2> ...
    ```
    (Exemplo: `T X A`)

* **Jogar uma Palavra:**
    ```
    J <linha> <coluna> <direção> <palavra>
    ```
    * `<linha>`: Um número de 1 a 15.
    * `<coluna>`: Um número de 1 a 15.
    * `<direção>`: `H` (Horizontal) ou `V` (Vertical).
    * (Exemplo: `J 8 8 H MUDO`)

### Definição de Jogadores (Agentes vs. Humanos)

Ao iniciar um jogo, é necessário definir os jogadores. Esta configuração distingue entre humanos e agentes (BOT's).

* **Jogadores Humanos:** São definidos por uma cadeia de carateres não vazia que representa o seu nome (ex: `'Jogador'`).
* **Jogadores Agentes (BOTs):** São definidos por uma cadeia de carateres que começa com `@` seguida do nível de dificuldade. [cite: 389]
    * `'@FACIL'` 
    * `'@MEDIO'` 
    * `'@DIFICIL'`

## Criar um Jogo Personalizado

Para iniciar uma nova partida, deve-se invocar a função principal `scrabble2` com os seguintes argumentos:

`scrabble2(jogadores, nome_fich, seed)`

* `jogadores`: Um ***tuplo*** contendo entre 2 a 4 cadeias de carateres que definem os jogadores e a sua ordem de jogada.
* `nome_fich`: Uma ***cadeia de carateres*** com o nome (e caminho) do ficheiro de texto que contém o vocabulário do jogo.
* `seed`: Um ***inteiro*** positivo usado como estado inicial (semente) para o gerador de números pseudoaleatórios, o que permite baralhar o saco de letras de forma reprodutível.

### Exemplo de Configuração de Jogo

Para iniciar um jogo com três jogadores (um humano chamado 'Maria' e dois agentes, 'MEDIO' e 'DIFICIL'), usando o vocabulário 'vocab25k.txt' e a semente '32':

```python
# Exemplo de chamada da função principal
jogadores = ('Maria', '@MEDIO', '@DIFICIL')
ficheiro_vocabulario = 'vocab25k.txt'
semente = 32

pontuacoes_finais = scrabble2(jogadores, ficheiro_vocabulario, semente)

print(f"O jogo terminou. Pontuações: {pontuacoes_finais}")
```