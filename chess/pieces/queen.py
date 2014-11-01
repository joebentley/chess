from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Queen(Piece):
    def render(self):
        if self.color == Color.white:
            return 'Q'
        else:
            return 'q'

    def valid_move(self, position):
        # Check for diagonal movement (for diagonal movement, dy/dx = 1)
        if abs(position.y - self.position.y) / abs(position.x - self.position.x) == 1:
            return True

        # Else check for horizontal and vertical linear movement
        if ((abs(position.x - self.position.x) > 0 and (position.y - self.position.y == 0)) or
            (abs(position.y - self.position.y) > 0 and (position.x - self.position.x == 0))):

            return True

        return False

