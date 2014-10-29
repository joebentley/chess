from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Queen(Piece):
    def render(self):
        if self.color == Color.white:
            return 'Q'
        else:
            return 'q'

    def validMove(self, position):
        # Check for diagonal movement
        pass

