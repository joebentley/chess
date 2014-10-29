
from chess.board import Board

class Game:
    def run(self):
        board = Board.initBoard()
        print(board.render())

