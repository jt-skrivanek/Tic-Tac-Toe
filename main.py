from player import HumanPlayer

class TicTacToe():
    def __init__(self, x_player, y_player) -> None:
        self.og_board = ["1","2","3","4","5","6","7","8","9"]
        self.board = [
            "1","2","3",
            "4","5","6",
            "7","8","9"
                ]
        self.turn = 0
        self.moves = [] # keeps track of moves made
        self.x_player = x_player
        self.y_player = y_player

    def draw_board(self):
        print( self.board[0]," ", self.board[1]," ", self.board[2])
        print( self.board[3]," ", self.board[4]," ", self.board[5])
        print( self.board[6]," ", self.board[7]," ", self.board[8])

    def insert(self):
        """position = int(input("<choose a position> "))-1
        if position not in self.moves:
            if self.turn:
                self.board[position] = "x"
                self.turn = 0
            else:
                self.board[position] = "o"
                self.turn = 1
            self.moves.append(position)"""
        try:
            if self.turn:
                # self.x_player.make_move()
                move = self.x_player.make_move()
                if self.board[move] == self.y_player.symbol:
                    print("0 already has a place here!")
                else:
                    self.board[move] = self.x_player.symbol
                    self.turn = 0

            else:
                # self.y_player.make_move()
                move = self.y_player.make_move()
                if self.board[move] == self.x_player.symbol:
                    print("X already has a place here!")
                else:
                    self.board[move] = self.y_player.symbol
                    self.turn = 1
                    self.moves.append(move)
        except ValueError:
            print("invalid value try again")
            pass # as the turn is still the same there is no need for anything else 

    def check_win(self):
        if self.check_row() or self.check_columns() or self.check_diagonal():
            if self.turn:
                print("the winner is o")
            else:
                print("the winner is x")
            return True

    def check_row(self):
        row_1 = self.board[0] == self.board[1] == self.board[2] 
        row_2 = self.board[3] == self.board[4] == self.board[5]
        row_3 = self.board[6] == self.board[7] == self.board[8]
        if row_1 or row_2 or row_3:
            return True

    def check_columns(self):
        column_1 = self.board[0] == self.board[3] == self.board[6]
        column_2 = self.board[1] == self.board[4] == self.board[7]
        column_3 = self.board[2] == self.board[5] == self.board[8]
        if column_1 or column_2 or column_3:
            return True

    def check_diagonal(self):
        diagonal_1 = self.board[0] == self.board[4] == self.board[8]
        diagonal_2 = self.board[2] == self.board[4] == self.board[6]
        if diagonal_1 or diagonal_2:
            return True

    def check_tie(self):
        if not ("1" in self.board or "2" in self.board or "3" in self.board or "4" in self.board or "5" in self.board or "6" in self.board or "7" in self.board or "8" in self.board or "9" in self.board):
            print("TIE")
            return False

def play(game_instance):
    tictac = game_instance
    play = True
    while play:
        tictac.draw_board()
        tictac.insert()
        end = tictac.check_win() or tictac.check_tie()
        if end:
            tictac.draw_board()
            play = False
    print("game ended mfs")

if __name__== "__main__":
    x_player = HumanPlayer("X")
    y_player = HumanPlayer("O")
    # game instance
    t = TicTacToe(x_player, y_player)
    play(t)
