# check functions
def draw_board(board):
    print()
    print("   ",board[0],"|", board[1],"|", board[2])
    print("   ---|---|---")
    print("   ",board[3],"|", board[4],"|", board[5])
    print("   ---|---|---")
    print("   ",board[6],"|", board[7],"|", board[8])
    print()

def check_win(board, turn):
    if check_row(board) or check_columns(board) or check_diagonal(board):
        if turn=="x":
            print("the winner is X")
        else:
            print("the winner is O")
        return True
  
def check_row(board):
    row_1 = board[0] == board[1] == board[2] 
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    if row_1 or row_2 or row_3:
        return True
    
def check_columns(board):
    column_1 = board[0] == board[3] == board[6]
    column_2 = board[1] == board[4] == board[7]
    column_3 = board[2] == board[5] == board[8]
    if column_1 or column_2 or column_3:
        return True

def check_diagonal(board):
    diagonal_1 = board[0] == board[4] == board[8]
    diagonal_2 = board[2] == board[4] == board[6]
    if diagonal_1 or diagonal_2:
        return True
   
def check_tie(board):
    if not ("1" in board or "2" in board or "3" in board or "4" in board or "5" in board or "6" in board or "7" in board or "8" in board or "9" in board):
        print("\n------TIE-----")
        return True

def empty_squares(board):
    return ' ' in board

def num_empty_squares(board):
    return board.count(' ')

def available_moves(board):
    return [i for i, x in enumerate(board) if x==" "]
