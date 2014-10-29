from chess.point import Point
from chess.pieces.color import Color
from chess.pieces.pawn import Pawn
from chess.pieces.bishop import Bishop
from chess.pieces.knight import Knight
from chess.pieces.rook import Rook
from chess.pieces.queen import Queen
from chess.pieces.king import King


# Generate a 2D matrix filling each cell with a given value
def init2D(rows, columns, value):
    return [[value for x in range(columns)] for x in range(rows)]


# The board is addressed such that board[0][0] is the upper left corner, which is a white square
class Board:
    def __init__(self, width = 8, height = 8):
        self.width = width
        self.height = height
        self.board = init2D(width, height, None)

    # Render board as a string with new lines between each row
    def render(self):
        output = ''

        # Loop through entire board
        for y in range(self.height):
            for x in range(self.width):
                square = self.board[y][x]

                # Render a blank square as an empty space
                if square == None:
                    output += ' '
                else:
                    output += square.render()

                # Add a newline if at the end of a row
                if x == self.width - 1:
                    output += '\n'

        return output


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

        return board
