from chess.point import Point
from chess.pieces.color import Color
from chess.pieces.pawn import Pawn
from chess.pieces.bishop import Bishop
from chess.pieces.knight import Knight
from chess.pieces.rook import Rook
from chess.pieces.queen import Queen
from chess.pieces.king import King
from chess.pieces.blank import Blank


# Generate a 2D matrix filling each cell with a given value
def init2D(rows, columns, value):
    return [[value for x in range(columns)] for x in range(rows)]


# The board is addressed such that board[0][0] is the upper left corner, which is a white square
class Board:
    """Holds data and methods for manipulating the current state of the game board.
       The board is addressed such that board[0][0] is the upper left corner, which
       is a white square.

       Members:
       board -- 2D list holding the pieces
       width, height -- width and height of 2D list
    """

    def __init__(self, width = 8, height = 8):
        self.width = width
        self.height = height
        self.board = init2D(width, height, None)

    def render(self):
        """Render the board as a string with new lines at the end of each row"""
        output = ''

        # Loop through entire board
        for y in range(self.height):
            for x in range(self.width):
                output += self.board[y][x].render()

                # Add a newline if at the end of a row
                if x == self.width - 1:
                    output += '\n'

        return output


    def getsquare(self, position):
        """Return piece at position"""
        return self.board[position.y][position.x]

    def setsquare(self, position, piece):
        """Set square at given position with piece"""
        self.board[position.y][position.x] = piece

    def piece_at(self, position):
        """Whether or not the square is occupied."""
        return not isinstance(self.board[position.y][position.x], Blank)

    def move_piece(self, from_position, to_position):
        """Move piece at from one position to another, overwriting
           the piece at the end position.

           Keyword arguments:
           from_position (Point) -- the position that holds the piece to move
           to_position   (Point) -- the position to move the piece to
        """
        # Get the piece from the old position and place in new position
        piece = self.getsquare(from_position)
        self.setsquare(to_position, piece)
        # Set the old position to be blank
        self.setsquare(from_position, Blank())
        # Update the piece's position
        piece.set_position(to_position)

    def point_on_board(self, position):
        """Check if position (Point) is on the board."""
        if (position.x < 0 or position.y < 0 or
            position.x > self.width - 1 or position.y > self.height - 1):

            return False

        return True


    def init_board():
        """Initialize a standard chessboard."""
        board = Board()

        # Spawn the black back row
        board.board[0][0] = Rook(Point(0, 0), Color.black)
        board.board[0][1] = Knight(Point(1, 0), Color.black)
        board.board[0][2] = Bishop(Point(2, 0), Color.black)
        board.board[0][3] = King(Point(3, 0), Color.black)
        board.board[0][4] = Queen(Point(4, 0), Color.black)
        board.board[0][5] = Bishop(Point(5, 0), Color.black)
        board.board[0][6] = Knight(Point(6, 0), Color.black)
        board.board[0][7] = Rook(Point(7, 0), Color.black)

        # Spawn the white back row
        board.board[7][0] = Rook(Point(0, 7), Color.white)
        board.board[7][1] = Knight(Point(1, 7), Color.white)
        board.board[7][2] = Bishop(Point(2, 7), Color.white)
        board.board[7][3] = King(Point(3, 7), Color.white)
        board.board[7][4] = Queen(Point(4, 7), Color.white)
        board.board[7][5] = Bishop(Point(5, 7), Color.white)
        board.board[7][6] = Knight(Point(6, 7), Color.white)
        board.board[7][7] = Rook(Point(7, 7), Color.white)

        # Spawn the black pawns
        for x in range(len(board.board[1])):
            board.board[1][x] = Pawn(Point(x, 1), Color.black)

        # Spawn the white pawns
        for x in range(len(board.board[6])):
            board.board[6][x] = Pawn(Point(x, 6), Color.white)

        # Fill the rest with blanks
        for y in range(2, 6):
            for x in range(len(board.board[y])):
                board.board[y][x] = Blank()

        return board

