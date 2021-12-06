class Player():
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        pass



class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self):
        move = int(input(f"choose a position {self.symbol} player: ")) - 1
        return move

class AiPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)