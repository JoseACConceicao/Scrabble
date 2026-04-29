"""
@file scrabble.py
@author ist1118656 (Jose Conceicao)
@brief Implementation of the Scrabble game for the FP 25/26 course.
Includes TADs for Board, Players, Vocabulary, and game logic.
"""

#region Square TAD

# The immutable Square TAD represents a single position on the Scrabble board.
# Internal Representation: A tuple (line, column) for immutability.

# region Constructor
def create_square(line, column):
    """
    @brief Creates a new board square (square).
    @param line Line number (1-15).
    @param column Column number (1-15).
    @return Tuple (line, column) representing the square.
    @exception ValueError If the arguments are invalid.
    """
    if (
        not isinstance(line, int)
        or not isinstance(column, int)
        or not 0 < line <= 15
        or not 0 < column <= 15
    ):
        raise ValueError("create_square: invalid arguments")

    return (line, column)

#endregion

# region Selectors
def get_column(square):
    """
    @brief Retrieves the column associated with the square.
    @param square Square tuple.
    @return Column index (int).
    """

    return square[1]


def get_line(square):
    """
    @brief Retrieves the line associated with the square.
    @param square Square tuple.
    @return Line index (int).
    """

    return square[0]

#endregion

# region Recognizer
def is_square(square):
    """
    @brief Validates if the argument is a valid Scrabble board square.
    @param square Argument to check.
    @return True if valid, False otherwise.
    """

    # Check if it is a tuple (the chosen representation)
    if isinstance(square, tuple):
        # Validate coordinate types
        if isinstance(get_column(square), int) and isinstance(get_line(square), int):
            # Check board boundaries
            if 1 <= get_column(square) <= 15 and 1 <= get_line(square) <= 15:
                return True
    else:
        return False  # If conditions are not met, it is not a valid square
#endregion

# region Testing
def squares_equal(square1, square2):
    """
    @brief Checks if two squares are identical.
    @param square1 First square.
    @param square2 Second square.
    @return True if equal, False otherwise.
    """

    return (
        True
        if get_line(square1) == get_line(square2) and get_column(square1) == get_column(square2)
        else False
    )

#endregion

# region Transformers
def square_to_str(square):
    """
    @brief Returns the string representation of a square.
    @param square Square tuple.
    @return String "(line,column)".
    """

    return str(square).replace(" ", "")


def str_to_square(text_str):
    """
    @brief Converts a string representation back to a square tuple.
    @param text_str String representation "(line,column)".
    @return Square tuple (line, column).
    """
    text_str_coordenadas_square = ""
    for char in text_str:
        if not char in {"(", ")", " "}:
            text_str_coordenadas_square += "".join(char)
    coordenadas = text_str_coordenadas_square.split(",")

    square = create_square(int(coordenadas[0]), int(coordenadas[1]))

    return square

#endregion

# region High-Level Functions
def increment_square(c, d, s):
    """
    @brief Returns the next square in a given direction and distance.
    @param c Starting square.
    @param d Direction ("V" for Vertical, "H" for Horizontal).
    @param s Distance to move.
    @return Next square tuple, or the original if move is invalid.
    """

    column_original = get_column(c)
    line_original = get_line(c)

    if d == "V":
        line = line_original + s
        column = column_original
    if d == "H":
        line = line_original
        column = column_original + s
    if 1 <= line <= 15 and 1 <= column <= 15:
        return create_square(line, column)
    else:
        return c

#endregion

#endregion


#region Player TAD

# The Player TAD represents a Scrabble player, their score, and held letters.
# Players can be human or AI agents.

# Internal Representation: A dictionary structure.

# region Constructors
def create_human (name):
    """
    @brief Creates a human Scrabble player.
    @param name Name of the player (non-empty string).
    @return Dictionary representing the human player.
    @exception ValueError If name is invalid.
    """
    
    if not isinstance(name, str) or name == '':
        raise ValueError('create_human: invalid argument')
    
    return {'name': name, 'score': 0, 'letters': ''}

def create_agent(level):
    """
    @brief Creates an AI agent Scrabble player.
    @param level AI level ('FACIL', 'MEDIO', or 'DIFICIL').
    @return Dictionary representing the agent player.
    @exception ValueError If level is invalid.
    """
    
    if not isinstance(level, str) or level not in {'FACIL', 'MEDIO', 'DIFICIL'}:
        raise ValueError("create_agent: invalid argument")
    
    return {'level': level, 'score': 0, 'letters': ''}
#endregion

#region Selectors
def player_identity (player):
    """
    @brief Retrieves the player's identity (name for humans, level for agents).
    @param player Player dictionary.
    @return String identity.
    """
    
    if 'level' in player: # AI Agent player
        return player['level']
    elif 'name' in player: # Human player
        return player['name']
    
def player_points(player):
    """
    @brief Retrieves the player's current score.
    @param player Player dictionary.
    @return Score (int).
    """
    
    return player['score']

def player_letters(player):
    """
    @brief Retrieves the sorted string of letters held by the player.
    @param player Player dictionary.
    @return Sorted string of letters.
    """
    
    return player['letters']
    
# endregion

# region Modificadores
def receive_letter (player, letter):
    """
    @brief Adds a letter to the player's collection (destructive).
    @param player Player dictionary.
    @param letter Letter string to add.
    @return Updated player dictionary.
    """
    
    new_letters = player['letters'] + "".join(letter)
    
    player['letters'] = "".join(sorted(new_letters, key = key_func))
    
    return player

def use_letter (player, letter):
    """
    @brief Removes a letter from the player's collection (destructive).
    @param player Player dictionary.
    @param letter Letter string to remove.
    @return Updated player dictionary.
    """
    
    player['letters'] = player['letters'].replace(letter, '', 1)
    
    return player

def add_points (player, score):
    """
    @brief Adds points to the player's score (destructive).
    @param player Player dictionary.
    @param score Points to add.
    @return Updated player dictionary.
    """
    
    player['score'] += score
    
    return player

# endregion

# region Reconhecedores
def is_player (arg):
    """
    @brief Validates if the argument is a valid Player TAD.
    @param arg Object to check.
    @return True if valid, False otherwise.
    """
    
    if not isinstance(arg, dict):
        return False
    
    if len(arg.keys()) != 3:
        return False
    
    if 'name' in arg:
        standard_keys_set = {'name', 'score', 'letters'}
        if type(arg['name']) != str:
            return False
    elif 'level' in arg:
        standard_keys_set = {'level', 'score', 'letters'}
        if type(arg['level']) != str:
            return False
    else:
        return False
    
    for key_func in arg:
       if key_func not in standard_keys_set:
           return False
       
    if type(arg['score']) != int or arg['score'] < 0:
        return False
    
    if type(arg['letters']) != str:
        return False
    
    return True

def is_human (arg):
    """
    @brief Checks if the argument is a human player.
    @param arg Object to check.
    @return True if human, False otherwise.
    """
    
    if is_player(arg):
        if 'name' in arg:
            return True
    
    return False

def is_agent (arg):
    """
    @brief Checks if the argument is an AI agent player.
    @param arg Object to check.
    @return True if agent, False otherwise.
    """
    
    if is_player(arg):
        if 'level' in arg:
            return True
    
    return False
    
#endregion

# region Teste
def players_equal (p1, p2):
    """
    @brief Checks if two players are identical in identity, score, and letters.
    @param p1 First player.
    @param p2 Second player.
    @return True if equal, False otherwise.
    """
    if is_human(p1) and is_human(p2):
        if p1['name'] == p2['name'] and p1['score'] == p2['score'] and p1['letters'] == p2['letters']:
            return True
    elif is_agent(p1) and is_agent(p2):
        if p1['level'] == p2['level'] and p1['score'] == p2['score'] and p1['letters'] == p2['letters']:
            return True
    
    return False

# endregion

#endregion

# region Transformer
def player_to_str(player):
    """
    @brief Returns the string representation of a player's status.
    @param player Player dictionary.
    @return Formatted string: "NAME (SCORE): L E T T E R S".
    """
    player_letters_str = add_character(player_letters(player), ' ')
    
    if is_human(player):
        return f'{player_identity(player)} ({player_points(player):>3}):{player_letters_str}'
    elif is_agent(player):
        return f'BOT({player_identity(player)}) ({player_points(player):>3}):{player_letters_str}'

# endregion

# region Funções de Alto Nível
def distribute_letters(player, sack, num):
    """
    @brief Distributes a set number of letters from the sack to the player.
    @details Modifies both the player hand and the sack list (destructive).
    @param player Player dictionary.
    @param sack List of available letters (sack).
    @param num Maximum number of letters to distribute.
    @return Updated player dictionary.
    """
    
    for i in range(0, num):
        if len(sack) == 0:                  # Only add a letter if the
            break                           # sack is not empty.
        
        # Add the last letter from the sack to the player's hand and remove it
        receive_letter(player, sack.pop())
    
    return player
    
 
# endregion

# endregion


#region Vocabulary TAD

# The Vocabulary TAD represents the set of valid words allowed in the game.
# It also calculates and stores word scores.

# The data structure is internally organized by word length and starting letter
# using a nested dictionary structure for optimized lookups.

# region Constructor
def create_vocabulary(words_tuple):
    """
    @brief Creates a vocabulary from a tuple of words.
    @param words_tuple Tuple of strings.
    @return Vocabulary dictionary structure.
    @exception ValueError If the input is invalid.
    """
    
    if not isinstance(words_tuple, tuple) or len(words_tuple) < 1:
        raise ValueError('create_vocabulary: invalid argument')
    
    vocabulary = {}
    for word in words_tuple:
        # Validate word requirements
        if type(word) != str or not 2 <= len(word) <= 15:
            raise ValueError('create_vocabulary: invalid argument')
        for letter in word:
            if letter not in {'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I',
                             'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'X', 'Z'}:
                raise ValueError('create_vocabulary: invalid argument')
        
            # Add word to structure
            if len(word) in vocabulary:
                if word[0] in vocabulary[len(word)]:
                    vocabulary[len(word)][word[0]] = vocabulary[len(word)][word[0]].union({word})
                else:
                    vocabulary[len(word)][word[0]] = {word}
            else:
                vocabulary[len(word)] = {}
                vocabulary[len(word)][word[0]] = {word}
    return vocabulary

# endregion

# region Selectors
def get_points(vocabulary, word):
    """
    @brief Calculates the score of a word based on the vocabulary.
    @param vocabulary Vocabulary dictionary.
    @param word Word string.
    @return Word score (int).
    """
    score = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4,
              'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2,
              'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}
    initial_letter = word[0]
    length = len(word)
    
    current_score_word = 0
    if word in vocabulary[length][initial_letter]: 
        for letter in word:
            current_score_word += score[letter]
    
    return current_score_word

def get_words (vocabulary, length, letter):
    """
    @brief Retrieves all words with a specific length and starting letter.
    @param vocabulary Vocabulary dictionary.
    @param length Word length.
    @param letter Starting letter.
    @return Tuple of (word, score) pairs, sorted by score and then alphabetically.
    """
    if letter not in vocabulary[length]:
        return ()
    
    pairs_tuple = ()
    for word in vocabulary[length][letter]:
        pairs_tuple += ((word, int(get_points(vocabulary, word))),)

    return tuple(sorted(pairs_tuple, key=lambda x: (-x[1], key_func(x[0]))))
    
        
# endregion

# region Testing
def test_word_pattern(vocabulary, word, pattern, letters):
    """
    @brief Checks if a word exists in the vocabulary and fits a given pattern.
    @details Validates if the player's letters can fill the pattern dots to form the word.
    @param vocabulary Vocabulary dictionary.
    @param word Word to test.
    @param pattern Board pattern string.
    @param letters Letters available in player's hand.
    @return True if word fits, False otherwise.
    """

    initial_letter = word[0]
    length = len(word)
    letters_player = letters
    
    # Verify if word exists in vocabulary for its length and initial letter
    words_by_letter = vocabulary.get(length, {}).get(initial_letter, set())
    if word not in words_by_letter:
        return False
    
    if length == len(pattern):
        for i in range(length):
            if pattern[i] != '.' and pattern[i] != word[i]:
                return False
            elif pattern[i] == '.':
                if word[i] not in letters_player:
                    return False
                letters_player = letters_player.replace(word[i], '', 1)
        
        return True
    
    else: 
        return False

# endregion

#endregion

# region Transformers
def file_to_vocabulary(filename):
    """
    @brief Loads a vocabulary from a text file.
    @details Reads each line, converts to uppercase, and filters valid 2-15 letter words.
    @param filename Path to the vocabulary file.
    @return Vocabulary dictionary structure.
    """
    
    with open(filename, 'r') as f:
        # Read all lines from file
        lines = f.readlines()
        
    
        valid_letters = {'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I',
                        'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'X', 'Z'}
        
        words_tuple = ()
        for line in lines:
            # Get uppercase word and strip newlines
            word = line.strip().upper()
            # Validate letters and length
            if 2 <= len(word) <= 15 and all(char in valid_letters for char in word):
                words_tuple += (word,)
        
        return create_vocabulary(words_tuple)
    

def vocabulary_to_str (vocabulary):
    """
    @brief Returns the full vocabulary content as a single newline-separated string.
    @details Words are ordered by length and then alphabetically.
    @param vocabulary Vocabulary dictionary.
    @return Multi-line string of all words.
    """

    words = []
    for length in sorted(vocabulary.keys()): # Ascending order of length
        for initial_letter in sorted(vocabulary[length]): # Lexicographical order of first character
            for word, _ in get_words(vocabulary, length, initial_letter):
                words.append(word) # get_words already returns correctly sorted pairs.
                
    return '\n'.join(words)
            
#endregion

# region High-Level Functions

def search_word_pattern(vocabulary, pattern, letters, min_score):
    """
    @brief Searches for the highest-scoring word that fits a given board pattern.
    @param vocabulary Vocabulary dictionary.
    @param pattern Board pattern string (letters and dots).
    @param letters Letters available in player's hand.
    @param min_score Minimum acceptable score to consider.
    @return Tuple of (best_word, score). Returns ('', 0) if no word fits.
    """
    
    length = len(pattern)
    current_score = 0
    chosen_word = ''

    # If this length does not exist in the vocabulary
    if length not in vocabulary:
        return ('', 0)

    # Pattern starts with a fixed letter
    if pattern[0] != '.':
        words = get_words(vocabulary, len(pattern), pattern[0])
        for pair_item in words:
            # Protect against unexpected inputs
            if not (isinstance(pair_item, tuple) and len(pair_item) >= 1):
                continue
            word = pair_item[0]
            # só testar word se ela for string
            if not isinstance(word, str):
                continue
            score_word = get_points(vocabulary, word)
            if score_word > current_score and test_word_pattern(vocabulary, word, pattern, letters):
                current_score = score_word
                chosen_word = word
            elif score_word == current_score and test_word_pattern(vocabulary, word, pattern, letters):
                if chosen_word == '' or word < chosen_word:
                    chosen_word = word

    # Pattern starts empty — try all letters from hand
    else:
        words = ()
        for letter in letters:
            # get_words should return a tuple of (word, score) pairs or ()
            pares = get_words(vocabulary, len(pattern), letter)
            if not pares:
                continue
            # Concatenate only if pairs is an iterable of pairs

        # Iterate over (word, score) tuples - protecting against invalid entries
        for item in words:
            if not (isinstance(item, tuple) and len(item) >= 1):
                continue
            word = item[0]
            if not isinstance(word, str):
                continue
            score_word = get_points(vocabulary, word)
            if score_word > current_score and test_word_pattern(vocabulary, word, pattern, letters):
                current_score = score_word
                chosen_word = word
            elif score_word == current_score and test_word_pattern(vocabulary, word, pattern, letters):
                if chosen_word == '' or word < chosen_word:
                    chosen_word = word

    return (chosen_word, current_score) if current_score >= min_score else ('', 0)
        
# endregion

#endregion


#region Board TAD

# Internal Representation: A 15x15 matrix (list of lists).
# The board TAD represents the Scrabble board and the letters placed on it.

# region Constructors
def create_board ():
    """
    @brief Creates a new empty Scrabble board.
    @return 15x15 matrix (list of lists) initialized with ".".
    """
    
    board = []
    for i in range(15):
        row = []
        for j in range(15):
            row.append(".")
        board.append(row)

    return board
#endregion

# region Selectors
def get_letter(board, square):
    """
    @brief Retrieves the letter at a given board position.
    @param board Board matrix.
    @param square Square tuple.
    @return Character at the position.
    """
    
    return board[get_line(square) - 1][get_column(square) - 1] # Map 1-based to 0-based

# endregion

# region Modificadores
def insert_letter(board, square, letter):
    """
    @brief Inserts a letter into the board (destructive).
    @param board Board matrix.
    @param square Square tuple.
    @param letter Letter string to insert.
    @return Updated board matrix.
    """
    board[get_line(square) - 1][get_column(square) - 1] = letter # Map 1-based to 0-based

    return board
#endregion

# region Recognizers
def is_board(arg):
    """
    @brief Validates if the argument is a valid Board TAD.
    @param arg Object to check.
    @return True if valid, False otherwise.
    """
    
    if type(arg) == list: # Confirm structure
        if len(arg) == 15: # Confirm number of rows
            for line in arg:
                if type(line) == list: # Confirm structure
                    if len(line) == 15: # Confirm number of columns
                        return True
            
    return False


def is_board_empty(arg):
    """
    @brief Checks if the board is empty (all positions are ".").
    @param arg Board object.
    @return True if empty, False otherwise.
    """
    if is_board(arg):
        for line in range(1, 16):
            for column in range (1, 16):
                if get_letter(arg, create_square(line, column)) != '.':
                    return False
        return True
    
    return False

# endregion

# region Teste
def boards_equal(arg1, arg2):
    """
    @brief Checks if two boards are identical in structure and content.
    @param arg1 First board.
    @param arg2 Second board.
    @return True if equal, False otherwise.
    """
    if is_board(arg1) and is_board(arg2): # Verify if both are boards
        for line in range(1, 16):
            for column in range (1, 16):
                if get_letter(arg1, create_square(line, column)) != get_letter(arg2, create_square(line, column)):
                    return False
        return True

# endregion

# region Transformador
def board_to_str(board):
    """
    @brief Returns a string representation of the board for printing.
    @param board Board matrix.
    @return Multi-line string with board coordinates and borders.
    """
    
    line_divider = "   +-------------------------------+"

    board_str = "                       1 1 1 1 1 1\n"  # Line 1
    board_str += "     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n"  # Line 2
    board_str += line_divider + '\n'  # Line 3

    # Add game rows
    for i in range(15):
        # Create string with row characters
        line = "".join(filter(character_filter, board[i]))

        # Add spaces to each row
        line = add_character(line, ' ')

        # Add borders to each row
        line = " |" + line + " |\n"

        # Add row to board string
        if i < 9:
            board_str = board_str + f" {i + 1}" + line # Alignment for single digits
        else:
            board_str = board_str + f"{i + 1}" + line  # Two digits, no extra space needed

    board_str += line_divider # Last line

    return board_str
#endregion

# region High-Level Functions
def get_pattern(board, square_i, square_f):
    """
    @brief Retrieves the sequence of letters between two board positions.
    @param board Board matrix.
    @param square_i Starting square.
    @param square_f Ending square.
    @return String of characters found in the specified range.
    @exception ValueError If squares are not in the same line or column.
    """
    
    line_i = get_line(square_i)
    line_f = get_line(square_f)
    
    column_i = get_column(square_i)
    column_f = get_column(square_f)
    
    pattern = ''
    
        
    if line_i == line_f:  # Squares are in the same line
        for column in range(column_i, column_f + 1):
            current_square = create_square(line_i, column)
            pattern += get_letter(board, current_square)
    
    elif column_i == column_f: # Squares are in the same column
        for line in range(line_i, line_f + 1):
            current_square = create_square(line, column_i)
            pattern += get_letter(board, current_square)
    else:
        raise ValueError("get_pattern: invalid arguments")
    
    return pattern


def insert_word(board, square, direction, word):
    """
    @brief Inserts a word onto the board (destructive).
    @param board Board matrix.
    @param square Starting square tuple.
    @param direction Direction ("V" or "H").
    @param word Word string to insert.
    @return Updated board matrix.
    """
    
    if direction == 'V':
        for i in range(len(word)):
            insert_letter(board, create_square(get_line(square) + i, get_column(square)), word[i])
    elif direction == 'H':
        for i in range(len(word)):
            insert_letter(board, create_square(get_line(square), get_column(square) + i), word[i])
    
    return board


def get_subpatterns (board, square_i, square_f, max_spaces):
    """
    @brief Generates all viable sub-patterns from a given board segment.
    @param board Board matrix.
    @param square_i Starting square.
    @param square_f Ending square.
    @param max_spaces Maximum allowed empty spaces (dots).
    @return Tuple of (sub-patterns, starting squares).
    """
    
    pattern = get_pattern(board, square_i, square_f)
    subpatterns_tuple = ()
    squares_tuple = ()
    
    for i in range(len(pattern)):
        for j in range(len(pattern), i, -1):  # ordem: mais longo primeiro
            subpattern = pattern[i:j]
            
            # Count empty spaces
            n_espacos = subpattern.count('.')
            if n_espacos == 0 or n_espacos > max_spaces:
                continue  # Valid patterns - rule 2 and maximum limit

            # Confirm there is at least one letter
            has_letter = any(c != '.' for c in subpattern)
            if not has_letter:
                continue  # rule 1

            # Confirm that it is not adjacent to other letters
            free_before = (i == 0) or (pattern[i - 1] == '.')
            free_after = (j == len(pattern)) or (pattern[j] == '.')
            if not (free_before and free_after):
                continue  # rule 3

            # Viable sub-pattern - store it
            subpatterns_tuple += (subpattern,)
            if get_line(square_i) == get_line(square_f):
                squares_tuple += (create_square(get_line(square_i), get_column(square_i) + i),)
            else:
                squares_tuple += (create_square(get_line(square_i) + i, get_column(square_i)),)
    
    return subpatterns_tuple , squares_tuple

def generate_all_patterns(board, max_spaces):
    """
    @brief Generates all viable patterns from the entire board.
    @param board Board matrix.
    @param max_spaces Maximum allowed dots per pattern.
    @return Tuple of (patterns, squares, directions).
    """
    
    subpatterns_tuple = ()
    squares_tuple = ()
    directions_tuple = ()
    
    # Horizontal patterns
    for line in range(1, 16):
        square_i = create_square(line, 1)
        square_f = create_square(line, 15)
        
        subpatterns, squares_i = get_subpatterns(board, square_i, square_f, max_spaces)
        
        subpatterns_tuple += subpatterns
        squares_tuple += squares_i
        directions_tuple += tuple('H' for _ in subpatterns)
        
    # Vertical patterns
    for column in range(1, 16):
        square_i = create_square(1, column)
        square_f = create_square(15, column)
        
        subpatterns, squares_i = get_subpatterns(board, square_i, square_f, max_spaces)
        
        subpatterns_tuple += subpatterns
        squares_tuple += squares_i
        directions_tuple += tuple('V' for _ in subpatterns)
    
    return subpatterns_tuple, squares_tuple, directions_tuple

#endregion

#endregion


#region Additional Functions

# Miscellaneous helper functions for game state and randomization.
def shuffle_sack(seed):
    """
    @brief Shuffles the Scrabble letter sack using a seed.
    @param seed Random generator seed.
    @return List of shuffled letters.
    """
    
    sack_dict = {'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11,
            'F': 2, 'G': 2, 'H': 2, 'I': 10, 'J': 2, 'L': 5,
            'M': 6, 'N': 4, 'O': 10, 'P': 4, 'Q': 1, 'R': 6,
            'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1 }

    shuffled_letters = set_elements(sack_dict)     # Create a list with all letters from the set (dict)

    permute_letters(shuffled_letters, seed)        # Shuffle the list

    return shuffled_letters


def human_move (board, player, vocabulary, sack):
    """
    @brief Processes a human player's turn.
    @param board Board matrix.
    @param player Player dictionary.
    @param vocabulary Vocabulary dictionary.
    @param sack Sack of letters (list).
    @return True if a move/swap was made, False if passed.
    """
    letters = [
            "A",
            "B",
            "C",
            "Ç",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "X",
            "Z",
        ]
    
    # Obtain move and process it:
    while True:
        
        is_valid_move = True # State Machine variable
        
        move_str = input(f"Move {player_identity(player)}: ")
        
        # Empty move
        if move_str == '':
            continue
        
        # Pass the move:
        elif move_str == 'P':
            return False
        
        # Swap letters
        elif move_str[0] == 'T':
            # Focus only on letters to swap
            move_str = move_str[2::]

            if len(move_str) % 2 == 0:
                is_valid_move = False
                
            if is_valid_move:
                # Check if letters are separated by " "
                for index in range(len(move_str)):
                    if index % 2 == 0 and not move_str[index] in player_letters(player):
                        is_valid_move = False
                        break
                    elif index % 2 == 1 and not move_str[index] == " ":
                        is_valid_move = False
                        break

            # Swap the letters
            if is_valid_move:
                letters_to_swap = move_str.split(' ')
                
                # Check if there are enough letters in the sack
                # Not enough letters in sack for swap
                # Player must try another move
                continue  # Return to start of loop for new attempt
                
                for letter in letters_to_swap:
                    player = use_letter(player, letter)
                
                player = distribute_letters(player, sack, len(letters_to_swap))
                
                return True

        # Place word
        elif move_str[0] == "J":
            if move_str.count(" ") != 4:
                is_valid_move = False
            else:
                # Split move into parts
                move_parts = move_str.split()
                
                if len(move_parts) < 5:
                    is_valid_move = False
                else:
                    # Assign move parts to specific variables
                    J, line_str, column_str, direction, word = move_parts

                    # Get word placement details
                    line = int(line_str)
                    column = int(column_str)
                    if direction not in ("H", "V"):
                        is_valid_move = False
                    if not (1 <= line <= 15 and 1 <= column <= 15):
                        is_valid_move = False

                    # Check if all letters are valid
                    for letter in word:
                        if letter not in letters:
                            is_valid_move = False
                            break
                
                if is_valid_move:
                    square_initial = create_square(line, column)
                    
                    if direction == 'V':
                        square_final = create_square(line + len(word) - 1, column)
                    elif direction == 'H':
                        square_final = create_square(line, column + len(word) - 1)
                        
                    pattern = get_pattern(board, square_initial, square_final)
                    
                    if not test_word_pattern(vocabulary, word, pattern, player_letters(player)):
                            is_valid_move = False

                    if is_valid_move:
                        
                        board = insert_word(board, square_initial, direction, word)
                        
                        move_score = get_points(vocabulary, word)
                        
                        player = add_points(player, move_score)
                        
                        # Remove played letters from player hand
                        letters_to_remove = []
                        for i in range(len(word)):
                            if pattern[i] == '.':
                                letters_to_remove.append(word[i])
                                
                        for letter in letters_to_remove:
                            player = use_letter(player, letter)
                        
                        # Replenish letters
                        player = distribute_letters(player, sack, len(letters_to_remove))
                        
                        return True


def agent_move (board, player, vocabulary, sack):
    """
    @brief Processes an AI agent's turn.
    @param board Board matrix.
    @param player Agent player dictionary.
    @param vocabulary Vocabulary dictionary.
    @param sack Sack of letters (list).
    @return True if a move/swap was made, False if passed.
    """
    
    
    # Pass
    if is_board_empty(board):
        print(f'Move {player_identity(player)}: P')
        return False
    
    # Play
    
    # Generate all patterns based on player hand size
    patterns, squares_i, directions= generate_all_patterns(board, len(player_letters(player)))
        
    # Slicing patterns based on agent level
    if player_identity(player) == 'FACIL':
        patterns = patterns[::100]
        squares_i = squares_i[::100]
        directions = directions[::100]
            
    elif player_identity(player) == 'MEDIO':
        patterns = patterns[::50]
        squares_i = squares_i[::50]
        directions = directions[::50]
            
    elif player_identity(player) == 'DIFICIL':
        patterns = patterns[::10]
        squares_i = squares_i[::10]
        directions = directions[::10]
        
    best_score = 0
    best_move = None
        
    for i in range(len(patterns)):
            
        pattern = patterns[i]
        square_i = squares_i[i]
        direction = directions[i]
            
        # Search for word for this pattern
            
        word, current_score = search_word_pattern(vocabulary, pattern, player_letters(player), best_score)
            
        # If a higher-scoring word is found, update best move
            
        if current_score > best_score:
            best_score = current_score
            best_move = (word, square_i, direction, pattern)
                
    # If a valid move was found
    if best_move and best_move[0]:  # Word is not empty
        word, square_i, direction, pattern = best_move
        
        # Insert word on board
        board = insert_word(board, square_i, direction, word)
            
        # Update score
        player = add_points(player, best_score)
            
        # Determine letters used (those filling dots)
        used_letters = []
        for i in range(len(word)):
            if pattern[i] == '.':
                used_letters.append(word[i])
                    
        # Remove letters
        for letter in used_letters:
            use_letter(player, letter)
                
        # Replenish hand
        distribute_letters(player, sack, len(used_letters))
        
        # Show move in correct format
        print(f"Move {player_identity(player)}: J {get_line(square_i)} {get_column(square_i)} {direction} {word}")
            
        return True
        
    # Swap - if no move was found and sack has enough letters
    elif len(sack) >= 7:
        # Store current letters for display
        letters_atuais = player_letters(player)
        
        # Remove letters
        for letter in player_letters(player):
            player = use_letter(player, letter)
            
        # Add new letters
        player = distribute_letters(player, sack, 7)
        
        # Show swap move
        letters_formatadas = ' '.join(letters_atuais)
        print(f"Move {player_identity(player)}: T {letters_formatadas}")
        
        return True
    
    else:
        print(f"Move {player_identity(player)}: P")
        return False
    
    
def scrabble2 (players, filename, seed):
    """
    @brief Main Scrabble game loop for 2-4 players.
    @param players Tuple of player names or agent levels (e.g., "@FACIL").
    @param filename Path to vocabulary file.
    @param seed Random generator seed.
    @return Tuple of final scores.
    @exception ValueError If arguments are invalid.
    """
    
    # Argument validation
    if (not isinstance(players, tuple) or not  2 <= len(players) <= 4 or
        not isinstance(filename, str) or filename == '' or
        not isinstance(seed, int) or seed <= 0):
        
        raise ValueError("scrabble2: invalid arguments")
    
    for j in players:
        if not isinstance(j, str) or j == '':
            raise ValueError('scrabble2: invalid arguments')
        if j[0] == '@' and len(j) == 1:
            raise ValueError('scrabble2: invalid arguments')
        if j[0] == '@':
            level = j[1:]
            if level not in {'FACIL', 'MEDIO', 'DIFICIL'}:
                raise ValueError('scrabble2: invalid arguments')
        
    # Initialization
    print("Welcome to SCRABBLE2.")
    
    board = create_board()
    
    sack = shuffle_sack(seed)
    
    vocabulary = file_to_vocabulary(filename)
    
    # Create player lists (humans and agents)
    players_list = []
    
    for name in players:
        if name[0] == '@':
            players_list.append(create_agent(name[1::].upper()))
        else:
            players_list.append(create_human(name))
            
    # Distribute 7 letters to each player
    for i in range(len(players_list)):
        players_list[i] = distribute_letters(players_list[i], sack, 7)
        
    # Main Loop
    consecutive_passes = 0
    num_players = len(players_list)
    game_over = False

    
    while not game_over:
        for i in range(num_players):
            
            # Interrupt game based on pass count
            if consecutive_passes >= num_players:
                game_over = True
                break
            
            
             # Print board
            print(board_to_str(board), '\n')
            
            # Print player status
            for player in players_list:
                print(player_to_str(player))
            
            print()
            
            player = players_list[i]
            
            
            
            # Turn
            name = player_identity(player)
            
            if is_agent(player):
                result = agent_move(board, player, vocabulary, sack)
            elif is_human(player):
                result = human_move(board, player, vocabulary, sack)
            
            # Check if player passed
            if result is False:
                consecutive_passes += 1
            else:
                consecutive_passes = 0
                
            # Check if player ran out of letters and sack is empty
            if len(player_letters(player)) == 0 and len(sack) == 0:
                game_over = True
                break
    
    # Final score calculation
    final_scores = tuple(player_points(player) for player in players_list)
    
    return final_scores
    

#endregion


# endregion


#region Helper Functions

def add_character(text_str, char):
    """
    @brief Inserts a character between every character in a string.
    @param text_str Original string.
    @param char Character to insert.
    @return Modified string.
    """
    index = 0
    while index <= len(text_str) -1:
        # Get substring up to index, add character, then append rest
        text_str = text_str[0:index:1] + f"{char}" + text_str[index : len(text_str) : 1]
        index += 2
    return text_str


def key_func(word):
    """
    @brief Sort key for lexicographical ordering of Scrabble words.
    @param word Word string.
    @return List of priority values.
    """
    
    alphabet = 'A B C Ç D E F G H I J L M N O P Q R S T U V X Z'.split()
    # Create priority dictionary
    priority = {letter: i for i, letter in enumerate(alphabet)}
    
    return [priority[letter] for letter in word]


def character_filter(ch):
    """
    @brief Filter function for board line elements.
    @param ch Character to evaluate.
    @return True if character should be kept, False if it's a delimiter.
    """

    if ch in ["[", "]", ","]:   # If character is in this list, remove it
        return False
    else:
        return True


def set_elements(collection):
    """
    @brief Converts a letter frequency dictionary into a sorted string of elements.
    @param collection Dictionary of {letter: count}.
    @return Sorted string of all elements.
    """

    keys = list(collection.keys())
    elements = ''

    for letter in keys:
        occ = collection[letter]
        for i in range(occ):
            elements += ''.join(letter)

    elements = sorted(elements, key=key_func)  # Use custom sort key defined above

    return elements

def permute_letters(letters, state):
    """
    @brief Permutes a sequence using the Fisher-Yates algorithm.
    @param letters List of letters to permute (destructive).
    @param state Random generator state.
    """

    n = len(letters)
    for i in range(n - 1, 0, -1):
        state = generate_random_number(state)
        j = state % (i + 1)
        letters[j], letters[i] = letters[i], letters[j]
        

def generate_random_number(state):
    """
    @brief Generates a pseudo-random number using the xorshift32 algorithm.
    @param state Current generator state.
    @return Next pseudo-random number.
    """

    state ^= (state << 13) & 0xFFFFFFFF
    state ^= (state >> 17) & 0xFFFFFFFF
    state ^= (state << 5) & 0xFFFFFFFF

    return state & 0xFFFFFFFF

#endregion






# Game Example

players_list = ('Leticia', '@MEDIO', '@DIFICIL', )

final_scores = scrabble2(players_list, 'vocab25k.txt', 32)

print(f"\nThe game has ended. Final Scores: {final_scores}\n")
