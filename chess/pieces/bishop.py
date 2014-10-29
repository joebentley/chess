from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Bishop(Piece):
    def render(self):
        if self.color == Color.white:
            return 'B'
        else:
            return 'b'

