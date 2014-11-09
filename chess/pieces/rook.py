from chess.pieces.color import Color
from chess.pieces.piece import Piece
from chess.point import Point

class Rook(Piece):
    def render(self):
        if self.color == Color.white:
            return 'R'
        else:
            return 'r'

    def valid_move(self, board, position):
        # Check if movement isn't horizontal or vertical
        if not (((abs(position.x - self.position.x) > 0 and
                 (position.y - self.position.y == 0)) or
                 (abs(position.y - self.position.y) > 0 and
                 (position.x - self.position.x == 0)))):

            return False


        # Check if there is a piece between the rook's position and its destination.

        # If the position delta is negative we need to range upwards,
        # delta/abs(delta) will give us a step of 1 or -1 depending on
        # whether or not the position delta is positive or negative
        y_delta = position.y - self.position.y
        x_delta = position.x - self.position.x

        if y_delta > 0:
            y_step = int(y_delta / abs(y_delta))

            # Start at 1 or -1, not 0, this is the same as the y_step
            for y in range(y_step, y_delta, y_step):
                if board.piece_at(Point(self.position.x, self.position.y + y)):
                    return False

        if x_delta > 0:
            x_step = int(x_delta / abs(x_delta))
            for x in range(x_step, x_delta, x_step):
                if board.piece_at(Point(self.position.x + x, self.position.y)):
                    return False

        return True

