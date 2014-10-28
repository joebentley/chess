
def init2D(rows, columns):
    [[0 for x in range(columns)] for x in range(rows)]

class Board:
    def __init__(self):
        self.board = init2D(10, 10)
