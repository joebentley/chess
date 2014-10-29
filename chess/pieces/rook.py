from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Rook(Piece):
    def render(self):
        if self.color == Color.white:
            return 'R'
        else:
            return 'r'


