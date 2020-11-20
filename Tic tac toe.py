board = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

b = """
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

def player_side():
    player2 = ""
    player1 = input("Choose X or O(letter): ")
    validation = False
    if player1 == "x" or player1 == "X" or player1 == "o" or player1 == "O":
        validation = True
    while not validation:
        if player1 == "x" or player1 == "X" or player1 == "o" or player1 == "O":
            validation = True
        elif player1 != "x" or player1 != "X" or player1 != "o" or player1 != "O":
            player1 = input("Error. Please enter 'X' or 'O': ")
    player1 = player1.upper()
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
    if i % 2 == 0:
        player = players[0]
    if i % 2 == 1:
        player = players[1]
    choice = input(f"{player}'s turn\nchose place from 1-9: ")
    validation = False
    while not validation:
        try:
            choice = int(choice)
            if choice in range(1, 10):
                validation = True
            else:
                choice = input("Please enter number 1-9: ")
        except ValueError:
            choice = input("Error. Please enter number 1-9: ")
    while not space_check(board, int(choice)):
        choice = int(input("This space isn't free. Choose another one from 1-9: "))
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
    
stats = []
turn = 1
while True:
    i = 1
    players = player_side()
    print(b)
    game_on = full_board_check(board)
    while not game_on:
        position = space_input(board, i, players)
        if i % 2 == 0:
            marker = players[1]
        else:
            marker = players[0]
        input_marker(board, marker, int(position))
        DisplayBoard(board)
        i += 1
        game_on = full_board_check(board)
        if win_check(board, marker):
            stats.append(f"{turn}) '{marker} won")
            print(f"'{marker}' won!")
            break
    if game_on:
        stats.append(f"{turn}) Draw")
        turn += 1
        print("It's a draw! Board id full")
    if not replay():
        break
    else:
        i = 1
        board = ['#'] * 10

