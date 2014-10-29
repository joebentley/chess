
import curses
from chess.board import Board

class CursesGame:
    def __init__(self):
        # Setup curses
        self.window = curses.initscr()
        self.window.keypad(1)
        curses.cbreak()
        curses.curs_set(0)

        # Setup position on screen
        self.offsetX = 2
        self.offsetY = 2

        # Initialize a new board
        self.board = Board.initBoard()

    # Draw board onto the screen
    def draw(self):
        for y in range(len(self.board.board)):
            for x in range(len(self.board.board[y])):
                # Draw the character at given point onto screen at offset (offsetX, offsetY)
                self.window.addch(y + self.offsetY, x + self.offsetX,
                        ord(self.board.board[y][x].render()))

    def update(self):
        # Draw the board
        self.draw()

        # Refresh the window
        self.window.clear()
        self.window.refresh()

