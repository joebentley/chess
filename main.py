#!/usr/local/bin/python3

from chess.app import App

def main():
    app = App(curses=True)
    app.run()

if __name__ == '__main__':
    main()
