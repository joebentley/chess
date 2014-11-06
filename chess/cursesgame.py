
import curses
from chess.point import Point
from chess.board import Board
from chess.log import log

class CursesGame:
    def __init__(self):
        # Setup position on screen
        self.offsetX = 0
        self.offsetY = 0

        # Initialize a new board
        self.board = Board.init_board()

    def draw(self, stdscr):
        """Draw the board onto stdscr."""
        for y, row in enumerate(self.board.board):
            for x, piece in enumerate(row):
                # Draw letters for each column
                if y == 0:
                    # Convert x-coordinate to lower case letter in alphabet
                    char = str(chr(x + 97)).upper()
                    stdscr.addch(self.offsetY, x + self.offsetX + 2, char)

                    # Draw horizontal rule
                    stdscr.addch(self.offsetY + 1, x + self.offsetX + 2, '-')
                # Draw numbers for each row
                if x == 0:
                    # Convert y-coordinate to number in sequence [8..1]
                    num = str(8 - y)
                    stdscr.addch(y + self.offsetY + 2, self.offsetX, num)

                    # Draw vertical rule
                    stdscr.addch(y + self.offsetY + 2, self.offsetX + 1, '|')

                # Draw the character at given point onto screen at offset (offsetX, offsetY)
                stdscr.addch(y + self.offsetY + 2, x + self.offsetX + 2,
                        ord(piece.render()))

    def reset_cursor(self, stdscr):
        """Move cursor to position underneath board."""
        stdscr.move(self.board.height + self.offsetY + 3, self.offsetX + 1)
        stdscr.refresh()

    def update(self, stdscr):
        """Main game loop, responsible for drawing and input."""
        # Re-enter curses echo mode so user can see what they type
        curses.echo()

        # Initialize by drawing board and moving cursor underneath it
        self.draw(stdscr)
        self.reset_cursor(stdscr)

        while True:
            # Clear the screen
            stdscr.clear()
            # Draw the board
            self.draw(stdscr)

            # Move the cursor underneath the board
            self.reset_cursor(stdscr)

            # Convert input from byte array to list of unicode format strings
            command = stdscr.getstr().decode('utf-8').split()

            if command[0] == 'move':
                # Check that both positions are given
                if len(command) >= 3:
                    from_position = Point.from_letters(command[1], self.board)
                    to_position = Point.from_letters(command[2], self.board)
                    self.board.move_piece(from_position, to_position)

            if command[0] == 'reset':
                self.board = Board.init_board()

            if command[0] == 'quit' or command[0] == 'q':
                return

            log(Point.to_letters(Point(0, 0), self.board))

    def run(self):
        """Launch main game loop."""
        # Setup curses and launch main game update loop
        curses.wrapper(self.update)

