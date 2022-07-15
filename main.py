def create_board(board):
    '''Create a board with three rows and three columns.'''
    for row in board:
        print('|',  end="")
        for slot in row:
            print(f" {slot} ", end="|")
        print()


def check_move(move):
    '''Check if user move equal to number and not out of board.'''
    if not move.isnumeric() or int(move) > 9 or int(move) < 1:
        print("This's not a valid position!")
        return False
    else:
        return True


def occupied_box(coords, board):
    '''Check if user move is on a free position.'''
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("This box is already occupied!")
        return True
    else:
        return False


def coordinates(move):
    '''Determine row and column according to user move.'''
    row = int(move / 3)
    col = move
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    '''Add user move to a position on a board.'''
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    '''Define which user has to make a move.'''
    if user:
        return "X"
    else:
        return "O"


def is_win(user, board):
    '''Check winning positions.'''
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False

def new_game():
    '''Offer user to restart the game or to quit.'''
    to_continue = input("Do you want to start new game. Type 'Y' or 'N': ").upper()
    if to_continue == 'Y':
        tic_toc_toe()
    else:
        print('GAME OVER')



def tic_toc_toe():
    print("WELCOME TO TIC TOC TOE! CAll A FRIEND AND HAVE FUN!")
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    user = True
    turns = 0

    while turns < 9:
        active_user = current_user(user)
        create_board(board)
        if turns == 0 or turns % 2 == 0:
            move = input("Player 'X' make your move to a position from 1 through 9: ")
        else:
            move = input("Player 'O' make your move to a position from 1 through 9: ")
        if not check_move(move):
            print("Please try again.")
            continue
        move = int(move) - 1
        coords = coordinates(move)
        if occupied_box(coords, board):
            print("Please try again")
            continue
        add_to_board(coords, board, active_user)
        if is_win(active_user, board):
            print(f"Player '{active_user.upper()}' won!")
            create_board(board)
            new_game()
            break

        turns += 1
        if turns == 9:
            print("Draw!")
            create_board(board)
            new_game()
        user = not user


tic_toc_toe()


















