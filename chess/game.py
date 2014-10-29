
from chess.board import Board

class Game:
    def update(self):
        board = Board.initBoard()
        print(board.render())
        input()

