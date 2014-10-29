from chess.point import Point
from chess.pieces.color import Color

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

