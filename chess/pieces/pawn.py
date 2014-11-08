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

    def valid_move(self, board, position):
        # Is piece is trying to move 2 spaces forward, check the middle space
        if abs(self.position.subtract(position).y) == 2:
            if board.piece_at(position.subtract(Point(0, self.move_dir))):
                return False

        # Pawn must stay in same column during movement
        if position.x == self.position.x:
            # First check if a piece is in front of the pawn
            if board.piece_at(position):
                return False

            if position.y == self.position.y + self.move_dir:
                return True
            # Check if it is the pawn's first turn, if it is it can move two spaces as well
            if not self.moved and position.y == self.position.y + self.move_dir * 2:
                return True

        log(str(position.subtract(self.position) == Point(1, self.move_dir)))
        # If there is a piece in a forward diagonal, we can take it
        if (position.subtract(self.position) == Point(1, self.move_dir) and
                board.piece_at(self.position.add(Point(1, self.move_dir)))):

            return True

        if (position.subtract(self.position) == Point(-1, self.move_dir) and
                board.piece_at(self.position.add(Point(-1, self.move_dir)))):

            return True

        return False

