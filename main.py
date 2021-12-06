import random
import math
import checkers

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
        checkers.check_win()

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



def play(x_player, y_player):
    global turn
    global board

    play = True
    while play:
        checkers.draw_board(board)
        insert(board)
        print("turn is now"+turn)
        end = checkers.check_win(board, turn) or checkers.check_tie(board)
        if end:
            checkers.draw_board(board)
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
