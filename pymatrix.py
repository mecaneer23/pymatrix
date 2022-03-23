#!/usr/bin/env python3

import curses
from random import choice
from string import ascii_letters, digits


def main(stdscr):
    CHARS = [*ascii_letters, *digits]
    ROWS = stdscr.getmaxyx()[0] - 1
    COLS = stdscr.getmaxyx()[1] - 1

    col_array = [0 for _ in range(COLS)]

    curses.curs_set(0)
    curses.use_default_colors()
    stdscr.nodelay(True)
    stdscr.timeout(100)

    while True:
        try:
            char = stdscr.getch()
        except KeyboardInterrupt:  # exit on ^C
            return
        if char in (113, 27):  # q or esc
            return
        for col in range(COLS):
            stdscr.addch(col_array[col], col, choice(CHARS))
            if col_array[col] == ROWS:
                col_array[col] = 0
            col_array[col] += choice((0, 1, 1))

if __name__ == "__main__":
    return_code = curses.wrapper(main)
    print(return_code) if return_code else exit()
