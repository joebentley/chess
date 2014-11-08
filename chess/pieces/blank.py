
from chess.pieces.piece import Piece

# Piece associated with blank square
class Blank(Piece):
    def valid_move(self, board, position):
        return False

    def render(self):
        return 'x'
