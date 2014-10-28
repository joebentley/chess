from point import Point
from enum import Enum

class Color(Enum):
    white = 0
    black = 1
    neither = 2

class Piece:
    color = Color.white
    position = Point(0, 0)

    def __init__(self, position, color):
        self.position = position
        self.color = color

    # Check if move from self.position to position is valid for this piece
    def validMove(self, position):
        return True

    # Return a textual representation of the piece
    def render(self):
        return ' '


class Pawn(Piece):
    def render(self):
        if self.color == Color.white:
            return 'P'
        else:
            return 'p'

    def validMove(self, position):
        # If positive, move down the board, else move up
        moveDir = -1

        # White moves up, black moves down
        if self.color == Color.black:
            moveDir = 1

        if position.x == self.x and position.y == self.y + moveDir:
            return True

class Bishop(Piece):
    def render(self):
        if self.color == Color.white:
            return 'B'
        else:
            return 'b'

class Knight(Piece):
     def render(self):
        if self.color == Color.white:
            return 'K'
        else:
            return 'k'

class Rook(Piece):
    def render(self):
        if self.color == Color.white:
            return 'R'
        else:
            return 'r'

class Queen(Piece):
    def render(self):
        if self.color == Color.white:
            return 'Q'
        else:
            return 'q'

class King(Piece):
    def render(self):
        if self.color == Color.white:
            return 'K'
        else:
            return 'k'

