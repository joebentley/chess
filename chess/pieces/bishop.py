from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Bishop(Piece):
    def render(self):
        if self.color == Color.white:
            return 'B'
        else:
            return 'b'

    def validMove(self, position):
        # Check for diagonal movement (for diagonal movement, dy/dx = 1)
        if abs(position.y - self.position.y) / abs(position.x - self.position.x) == 1:
            return True


