from chess.point import Point
from chess.pieces.color import Color

class Piece:
    color = Color.white
    position = Point(0, 0)

    def __init__(self, position = Point(0, 0), color = Color.neither):
        self.position = position
        self.color = color

    # Return a list of all position the piece could reach
    def pointInReach(self, board):
        results = []

        for y, row in enumerate(self.board.board):
            for x, _ in enumerate(row):
                position = Point(x, y)

                if self.validMove(position):
                    results.append(position)

    # Return a textual representation of the piece
    def render(self):
        return ' '

