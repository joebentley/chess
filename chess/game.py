
from chess.board import Board

class Game:
    def update(self):
        while True:
            board = Board.initBoard()
            print(board.render())
            input()

    def run(self):
        self.update()

