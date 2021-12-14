import checkers
import random
# player class
class HumanPlayer():
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        move = int(input(f"choose a position {self.symbol} player: ")) - 1
        return move

    def moveAI(self):
        move = random.randint(0,8)
        return move
