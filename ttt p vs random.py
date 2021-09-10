import random

board = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

p = """
_______________________________
|         |         |         |
|    7    |    8    |    9    |
|_________|_________|_________|
|         |         |         |
|    4    |    5    |    6    |
|_________|_________|_________|
|         |         |         |
|    1    |    2    |    3    |
|_________|_________|_________|
"""
def DisplayBoard(board): 
    BlankBoard = """
_______________________________
|         |         |         |
|    7    |    8    |    9    |
|_________|_________|_________|
|         |         |         |
|    4    |    5    |    6    |
|_________|_________|_________|
|         |         |         |
|    1    |    2    |    3    |
|_________|_________|_________|
"""
    for i in range(1,10):
        if board[i] == "O" or board[i] == "X":
            BlankBoard = BlankBoard.replace(str(i), board[i])
        else:
            BlankBoard = BlankBoard.replace(str(i), ' ')
    print(BlankBoard)
    return BlankBoard

def player_side():
    player2 = ""
    player1 = (input("Choose X or O(letter): ")).upper()
    validation = False
    if player1 == "X" or player1 == "O":
        validation = True
    while not validation:
        if player1 == "X" or player1 == "O":
            validation = True
        else:
            player1 = (input("Error. Please enter 'X' or 'O': ")).upper()
    if player1 == "X":
        player2 = "O"
        return player2, player1
    if player1 == "O":
        player2 = "X"
        return player2, player1

def input_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == "#"

def space_input(board, i, players):
    inputText = "Invalid input. Choose another space from 1-9: "
    n = 10
    if i % 2 == 0:
        player = players[0]
        choice = random.randint(1, 9)
    if i % 2 == 1:
        player = players[1]
        choice = input(f"{player}'s turn\nchose place from 1-9: ")
        choice = input_control(choice, inputText, n, False)
    while not space_check(board, choice):
        if i % 2 == 1:
            choice = input_control(input("This space isn't free. Choose another one from 1-9: "), inputText, n, False)
        if i % 2 == 0:
            choice = random.randint(1, 9)
    return choice

def full_board_check(board):
    filteredBoard = []
    for x in board:
        if x == '#':
            filteredBoard.append(x)
    return (len(filteredBoard) == 1)

def win_check(board, marker):
    if board[1] == board[2] == board[3] == marker:
        return True
    if board[4] == board[5] == board[6] == marker:
        return True
    if board[7] == board[8] == board[9] == marker:
        return True
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    if board[3] == board[6] == board[9] == marker:
        return True
    if board[1] == board[5] == board[9] == marker:
        return True
    if board[3] == board[5] == board[7] == marker:
        return True
    return False

def replay():
    question = input("Do you want to play again 'y' or 'n': ")
    validation = False
    while not validation:
        if question == "y" or question == "n" or question == "Y" or question == "N":
            validation = True
        elif question != "y" or question != "n" or question != "Y" or question != "N":
            question = input("Error. Please enter 'y' or 'n'")
    if question == "y":
        return True
    if question == "n":
        print("_"*35, "Your stats: ", *stats, sep = "\n")
        return False

def input_control(choice, inputText, n, q):
    validation = False
    while not validation:
        if q == True:
            if choice == "n":
                return choice
        try:
            choice = int(choice)
            if choice in range(1, n):
                return choice
            else:
                choice = input(inputText)
        except ValueError:
            choice = input(inputText)

stats = []
b = ["#"]
turn = 1
inputText = ""

while True:
    i = 1
    players = player_side()
    print(p)
    game_on = full_board_check(board)
    while not game_on:
        position = space_input(board, i, players)
        if i % 2 == 0:
            marker = players[0]
        else:
            marker = players[1]
        input_marker(board, marker, position)
        DisplayBoard(board)
        i += 1
        game_on = full_board_check(board)
        if win_check(board, marker):
            result = DisplayBoard(board)
            stats.append(f"{turn}) '{marker}' won")
            b.append(result)
            turn += 1
            print(f"'{marker}' won!")
            break
        elif game_on:
            stats.append(f"{turn}) Draw")
            turn += 1
            print("It's a draw! Board is full")
    if not replay():
        while True:
            inputText = "Choose any turn to see the board or enter 'n' to exit: "
            g = input_control(input(inputText), inputText, turn, True)
            if g == "n":
                break
            print(b[g])
            print(*stats, sep = "\n")
        break
    else:
        i = 1
        
 dadada
