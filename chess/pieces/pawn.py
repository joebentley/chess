from chess.pieces.color import Color
from chess.pieces.piece import Piece
from chess.point import Point
from chess.log import log

class Pawn(Piece):
    def __init__(self, position = Point(0, 0), color = Color.neither):
        super().__init__(position, color)

        # If positive, move down the board, else move up
        self.move_dir = -1
        # White moves up, black moves down
        if self.color == Color.black:
            self.move_dir = 1

        # True if the piece hasn't moved yet
        self.moved = False

    def render(self):
        if self.color == Color.white:
            return 'P'
        else:
            return 'p'

    def valid_move(self, position):
        # Pawn must stay in same column during movement
        if position.x == self.position.x:
            if position.y == self.position.y + self.move_dir:
                return True
            # Check if it is the pawn's first turn, if it is it can move two spaces as well
            if not self.moved and position.y == self.position.y + self.move_dir * 2:
                return True

        return False

    def is_path_clear(self, board, to_pos):
        if board.piece_at(to_pos):
            return False
        # Is piece is trying to move 2 spaces, if so check the middle space
        if abs(self.position.subtract(to_pos).y) == 2:
            if board.piece_at(to_pos.subtract(Point(0, self.move_dir))):
                return False

        return True
