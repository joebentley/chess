from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Rook(Piece):
    def render(self):
        if self.color == Color.white:
            return 'R'
        else:
            return 'r'

    def valid_move(self, position):
        # Check for horizontal and vertical movement
        if ((abs(position.x - self.position.x) > 0 and (position.y - self.position.y == 0)) or
            (abs(position.y - self.position.y) > 0 and (position.x - self.position.x == 0))):

            return True

        return False

