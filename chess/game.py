
from chess.board import Board

class Game:
    def update(self):
        while True:
            board = Board.init_board()
            print(board.render())
            input()

    def run(self):
        self.update()

