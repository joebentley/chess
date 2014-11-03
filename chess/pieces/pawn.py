from chess.pieces.color import Color
from chess.pieces.piece import Piece
from chess.point import Point

class Pawn(Piece):
    def __init__(self, position = Point(0, 0), color = Color.neither):
        super().__init__(position, color)

        # If positive, move down the board, else move up
        self.moveDir = -1
        # White moves up, black moves down
        if self.color == Color.black:
            self.moveDir = 1

        # True if the piece hasn't moved yet
        self.moved = False

    def render(self):
        if self.color == Color.white:
            return 'P'
        else:
            return 'p'

    def moveDistance(self):
        """Return signed move distance that the piece can move."""
        return self.moveDir if self.moved else self.moveDir * 2

    def valid_move(self, position):
        if position.x == self.position.x and position.y == self.position.y + self.moveDistance():
            return True
        return False

    def is_path_clear(self, board, to_pos):
        if (board.piece_at(to_pos) or
            board.piece_at(self.position.add(Point(0, self.moveDistance())))):

            return False

        return True
