from chess.pieces.color import Color
from chess.pieces.piece import Piece
from chess.point import Point

class Bishop(Piece):
    def render(self):
        if self.color == Color.white:
            return 'B'
        else:
            return 'b'

    def valid_move(self, board, position):
        # Check for non-diagonal movement (for diagonal movement, dy/dx = 1)
        if not abs(position.y - self.position.y) / abs(position.x - self.position.x) == 1:
            return False

        # Cycle through each square between the current square and the destination
        # checking for other pieces
        x_delta = position.x - self.position.x
        y_delta = position.y - self.position.y

        x_step = int(x_delta / abs(x_delta))
        y_step = int(y_delta / abs(y_delta))

        for x in range(x_step, x_delta, x_step):
            for y in range(y_step, y_delta, y_step):
                # If there is another piece anywhere between the current
                # and destination square, this is not allowed
                if board.piece_at(Point(self.position.x + x, self.position.y + y)):
                    return False

        return True

