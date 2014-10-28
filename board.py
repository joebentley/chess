from point import Point
from piece import *

def init2D(rows, columns, value):
    return [[value for x in range(columns)] for x in range(rows)]

# The board is addressed such that board[0][0] is the upper left corner, which is a white square
class Board:
    def __init__(self):
        self.board = init2D(8, 8, None)

    # Render board as a string

    # Initialize a board as standard in chess
    def initBoard():
        board = Board()

        # Spawn the black back row
        board.board[0][0] = Rook(Point(0, 0), Color.black)
        board.board[0][1] = Knight(Point(0, 0), Color.black)
        board.board[0][2] = Bishop(Point(0, 0), Color.black)
        board.board[0][3] = King(Point(0, 0), Color.black)
        board.board[0][4] = Queen(Point(0, 0), Color.black)
        board.board[0][5] = Bishop(Point(0, 0), Color.black)
        board.board[0][6] = Knight(Point(0, 0), Color.black)
        board.board[0][7] = Rook(Point(0, 0), Color.black)

        # Spawn the white back row
        board.board[0][0] = Rook(Point(0, 0), Color.white)
        board.board[0][1] = Knight(Point(0, 0), Color.white)
        board.board[0][2] = Bishop(Point(0, 0), Color.white)
        board.board[0][3] = King(Point(0, 0), Color.white)
        board.board[0][4] = Queen(Point(0, 0), Color.white)
        board.board[0][5] = Bishop(Point(0, 0), Color.white)
        board.board[0][6] = Knight(Point(0, 0), Color.white)
        board.board[0][7] = Rook(Point(0, 0), Color.white)

        # Spawn the black pawns
        for x in range(len(board.board[1])):
            board.board[1][x] = Pawn(Point(x, 1), Color.black)

        # Spawn the white pawns
        for x in range(len(board.board[7])):
            board.board[7][x] = Pawn(Point(x, 7), Color.white)

        return board
