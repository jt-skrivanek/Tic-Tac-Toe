import checkers
from player import HumanPlayer, AiPlayer
"""------------------------------º---------------------------º--------------------------------------"""
og_board = ["1","2","3","4","5","6","7","8","9"]
board = [
        "1","2","3",
        "4","5","6",
        "7","8","9"
            ]
turn = "x"
moves = [] # keeps track of moves made

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

#m