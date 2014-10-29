
from chess.pieces.piece import Piece

# Piece associated with blank square
class Blank(Piece):
    def validMove(self):
        return False

    def render(self):
        return 'x'
