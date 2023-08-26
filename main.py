import curses
from curses import wrapper
from threading import Thread

key = ""

def handleKeys(stdscr):
    global key
    key = stdscr.getkey()
    stdscr.clear()
    stdscr.addstr("LatestDetectedKeyPress: " + str(key))

def main(stdscr):
    global key
    print("start")
    stdscr.nodelay(True)
    while True:
        try:

            handleKeys(stdscr)

            if key == "/":
                break

        except curses.error:
            pass

wrapper(main)