# FP - Scrabble Game / Jogo Scrabble

[English](#english) | [Português](#português)

---

## English

### Project Overview
This project was developed for the **FP (Fundamentals of Programming)** course at **Instituto Superior Técnico (IST)**. It implements a fully functional Scrabble game in Python, allowing matches between human players and AI agents with different difficulty levels.

### Key Objectives
- Implement Abstract Data Types (TADs) to represent game elements (Board, Player, Vocabulary).
- Develop a robust game engine capable of validating moves according to Scrabble rules.
- Design AI agents with varying strategies (Easy, Medium, Hard) using pattern matching and scoring heuristics.

### Features
- **Data-Driven Vocabulary**: Efficient word lookups and scoring using optimized dictionary structures.
- **AI Agents**: Automated players that simulate different skill levels by adjusting their search breadth and scoring priorities.
- **Interactive Gameplay**: A command-line interface for human players to manage their letters, swap tiles, and place words on the 15x15 board.

### Game Commands
When it is your turn, use the following commands:
- **Play Word**: `J <line> <column> <direction> <word>`
    - Example: `J 8 8 H PYTHON` (Places "PYTHON" starting at (8,8) horizontally).
    - `direction`: `H` for Horizontal, `V` for Vertical.
- **Swap Letters**: `T <L1> <L2> ...`
    - Example: `T A B` (Swaps letters 'A' and 'B' for new ones from the sack).
- **Pass**: `P`
    - Skips your turn. If all players pass consecutively, the game ends.

### Visual Example
Here is how the game looks in the terminal:
```text
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . P Y T H O N . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . C . . . . . |
11 | . . . . . . . . . R . . . . . |
12 | . . . . . . . . . A . . . . . |
13 | . . . . . . . . . B . . . . . |
14 | . . . . . . . . . B . . . . . |
15 | . . . . . . . . . L . . . . . |
   +-------------------------------+
```



---

## Português

### Resumo do Projeto
Este projeto foi desenvolvido no âmbito da Unidade Curricular de **FP (Fundamentos da Programação)** no **Instituto Superior Técnico (IST)**. Consiste numa implementação completa do jogo Scrabble em Python, permitindo partidas entre jogadores humanos e agentes de inteligência artificial com diferentes níveis de dificuldade.

### Objetivos Principais
- Implementar Tipos Abstratos de Dados (TADs) para representar os elementos do jogo (Tabuleiro, Jogador, Vocabulário).
- Desenvolver um motor de jogo robusto capaz de validar jogadas de acordo com as regras oficiais.
- Desenhar agentes de IA com estratégias variadas (Fácil, Médio, Difícil) utilizando padrões de pesquisa e heurísticas de pontuação.

### Funcionalidades
- **Vocabulário Otimizado**: Pesquisa eficiente de palavras e cálculo de pontuações através de estruturas de dicionários otimizadas.
- **Agentes de IA**: Jogadores automáticos que simulam diferentes níveis de habilidade, ajustando a largura da pesquisa e as prioridades de pontuação.
- **Jogabilidade Interativa**: Interface de linha de comandos para jogadores humanos gerirem as suas letras, trocarem peças e colocarem palavras no tabuleiro 15x15.

### Comandos de Jogo
Quando for o seu turno, utilize os seguintes comandos:
- **Jogar Palavra**: `J <linha> <coluna> <direção> <palavra>`
    - Exemplo: `J 8 8 H PYTHON` (Coloca "PYTHON" com início em (8,8) na horizontal).
    - `direção`: `H` para Horizontal, `V` para Vertical.
- **Trocar Letras**: `T <L1> <L2> ...`
    - Exemplo: `T A B` (Troca as letras 'A' e 'B' por novas peças do saco).
- **Passar**: `P`
    - Salta o seu turno. Se todos os jogadores passarem consecutivamente, o jogo termina.

### Exemplo Visual
Exemplo de como o jogo aparece no terminal:
```text
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . P Y T H O N . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . C . . . . . |
11 | . . . . . . . . . R . . . . . |
12 | . . . . . . . . . A . . . . . |
13 | . . . . . . . . . B . . . . . |
14 | . . . . . . . . . B . . . . . |
15 | . . . . . . . . . L . . . . . |
   +-------------------------------+
```