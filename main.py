#!/usr/local/bin/python3

from piece import *
from board import Board

def main():
    board = Board.initBoard()
    print(board.board)

if __name__ == '__main__':
    main()
