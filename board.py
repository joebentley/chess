from point import Point
from piece import *

def init2D(rows, columns, value):
    return [[value for x in range(columns)] for x in range(rows)]

# The board is addressed such that board[0][0] is the upper left corner, which is a white square
class Board:
    def __init__(self):
        self.board = init2D(8, 8, None)

    # Render board as a string
    def render(self):
        for y in range(7):
            for x in range(7):
                print(self.board[x][y].render())
                if x == 7:
                    print()

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
        board.board[7][0] = Rook(Point(0, 0), Color.white)
        board.board[7][1] = Knight(Point(0, 0), Color.white)
        board.board[7][2] = Bishop(Point(0, 0), Color.white)
        board.board[7][3] = King(Point(0, 0), Color.white)
        board.board[7][4] = Queen(Point(0, 0), Color.white)
        board.board[7][5] = Bishop(Point(0, 0), Color.white)
        board.board[7][6] = Knight(Point(0, 0), Color.white)
        board.board[7][7] = Rook(Point(0, 0), Color.white)

        # Spawn the black pawns
        for x in range(len(board.board[1])):
            board.board[1][x] = Pawn(Point(x, 1), Color.black)

        # Spawn the white pawns
        for x in range(len(board.board[6])):
            board.board[6][x] = Pawn(Point(x, 6), Color.white)

        # Fill the rest with blank pieces
        for x in range(len(board.board[7])):
            board.board[2][x] = Piece(Point(x, 2), Color.neither)
            board.board[3][x] = Piece(Point(x, 3), Color.neither)
            board.board[4][x] = Piece(Point(x, 4), Color.neither)
            board.board[5][x] = Piece(Point(x, 5), Color.neither)

        return board
