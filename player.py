import random
import math
import checkers


class HumanPlayer():
    def __init__(self, symbol):
        self.symbol = symbol

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
