import random
import math

og_board = ["1","2","3","4","5","6","7","8","9"]
board = [
        "1","2","3",
        "4","5","6",
        "7","8","9"
            ]
turn = "x"
moves = [] # keeps track of moves made

class HumanPlayer():
    def __init__(self, symbol):
        self.symbol = symbol
        self.board = board

    def make_move(self):
        move = int(input(f"choose a position {self.symbol} player: ")) - 1
        return move

class AiPlayer():
    def __init__(self, symbol, board):
        self.symbol = symbol
        self.board = board

    def make_move(self, game, board):
        if len(game.available_moves()) ==9: #meaning the start of the game
            move = random.choice(game.available_moves())
        else: #if a move has already been made
            move = self.minimax(board, self.symbol)
        return move

    def minimax(board,depth,symbol): #returns int meaning move
        max_player = symbol #AI symbol
        other_player = 'o' if symbol == 'x' else 'x'

        #first we check if we are in a win situation
        check_win()

"""------------------------------º---------------------------º--------------------------------------"""

x_player = HumanPlayer("x")
y_player = HumanPlayer("y")

def insert(board):
    global turn
    try:
        if turn == "x":
            # self.x_player.make_move()
            move = x_player.make_move()
            # checks to see if y player already has 0 here
            if board[move] == y_player.symbol or board[move] == x_player.symbol:
                print("INVALID PLACE!")
            else:
                board[move] = x_player.symbol
                turn = "y"
                print("here")
                moves.append(move)

        else:
            # y_player.make_move()
            move = y_player.make_move()
            # checks to see if x player already has X here
            if board[move] == x_player.symbol or board[move] == y_player.symbol:
                print("INVALID PLACE!")
            else:
                board[move] = y_player.symbol
                turn = "x"
                moves.append(move)
    except IndexError or ValueError:
        print("invalid value try again")
        pass # as the turn is still the same there is no need for anything else 


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
        if turn==1:
            print("the winner is o")
        else:
            print("the winner is x")
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

def play(x_player, y_player):
    global turn
    global board

    play = True
    while play:
        draw_board(board)
        insert(board)
        print("turn is now"+turn)
        end = check_win(board, turn) or check_tie(board)
        if end:
            draw_board(board)
            # play = False
            play_again = input("Play again? [y/n]").lower()

            if play_again == "y":
                board = og_board

            else:
                print("game ending....")
                play = False
    print("game ended mfs")

if __name__== "__main__":


    play(x_player, y_player)
