from chess.pieces.color import Color
from chess.pieces.piece import Piece

class King(Piece):
    def render(self):
        if self.color == Color.white:
            return 'K'
        else:
            return 'k'

