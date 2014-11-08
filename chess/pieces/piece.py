from chess.point import Point
from chess.pieces.color import Color

class Piece:
    color = Color.white
    position = Point(0, 0)

    def __init__(self, position = Point(0, 0), color = Color.neither):
        self.position = position
        self.color = color

    # Return a list of all position the piece could reach
    def points_in_reach(self, board):
        results = []

        for y, row in enumerate(self.board.board):
            for x, _ in enumerate(row):
                position = Point(x, y)

                if self.valid_move(position):
                    results.append(position)

    def set_position(self, position):
        """Set new position to position and sets self.moved.
           Calling this will not change position on board,
           for that use board.move_piece()

           Keyword arguments:
           position (Point) -- new position to move to """

        self.position = position
        self.moved = True

    # Return a textual representation of the piece
    def render(self):
        return ' '

    def __str__(self):
        return self.render()

