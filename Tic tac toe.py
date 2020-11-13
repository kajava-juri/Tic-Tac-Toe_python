board = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
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

def space_input(board):
    choice = int(input("chose place from 1-9: "))
    while not space_check(board, int(choice)):
        choice = int(input("This space isn't free. Choose another one from 1-9: "))
    return choice

def full_board_check(board):
    filteredBoard = []
    for x in board:
        if x == '#':
            filteredBoard.append(x)
    return (len(filteredBoard) == 1)

while True:
    i = 1
    players = player_side()
    game_on = full_board_check(board)
    while not game_on:
        position = space_input(board)
        if i % 2 == 0:
            marker = players[1]
        else:
            marker = players[0]
        input_marker(board, marker, int(position))
        DisplayBoard(board)
        i += 1
        game_on = full_board_check(board)
    #replay
    #
    #
    #.......

