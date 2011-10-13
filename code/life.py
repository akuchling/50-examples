#!/usr/bin/env python3

# life.py -- A turtle-based version of Conway's Game of Life.
#
# An empty board will be displayed, and the following commands are available:
#  E : Erase the board
#  R : Fill the board randomly
#  S : Step for a single generation
#  C : Update continuously until a key is struck
#  Q : Quit
#  Cursor keys :  Move the cursor around the board
#  Space or Enter : Toggle the contents of the cursor's position
#
# TODO :
#   Support the mouse
#   Use colour if available
#   Make board updates faster
#

import turtle
import random

CELL_SIZE = 10                  # Measured in pixels

class LifeBoard:
    """Encapsulates a Life board

    Attributes:
    X,Y : horizontal and vertical size of the board
    state : dictionary mapping (x,y) to 0 or 1

    Methods:
    display(update_board) -- If update_board is true, compute the
                             next generation.  Then display the state
                             of the board and refresh the screen.
    erase() -- clear the entire board
    makeRandom() -- fill the board randomly
    set(y,x) -- set the given cell to Live; doesn't refresh the screen
    toggle(y,x) -- change the given cell from live to dead, or vice
                   versa, and refresh the screen display

    """
    def __init__(self, xsize, ysize):
        """Create a new LifeBoard instance.

        scr -- curses screen object to use for display
        char -- character used to render live cells (default: '*')
        """
        self.state = {}
        self.X, self.Y = xsize, ysize

    def set(self, x, y):
        """Set a cell to the live state"""
        if x<0 or self.X<=x or y<0 or self.Y<=y:
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                    (x, y, self.X, self,Y)))
                             
        key = (x,y)
        self.state[key] = 1

    def toggle(self, x, y):
        """Toggle a cell's state between live and dead"""
        if x<0 or self.X<=x or y<0 or self.Y<=y:
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                    (x, y, self.X, self,Y)))
        key = (x,y)
        if self.state.has_key(key):
            del self.state[key]
        else:
            self.state[key] = None

    def erase(self):
        """Clear the entire board"""
        self.state.clear()

    def step(self):
        "Compute one generation, updating the display."
        d = {}
        for i in range(0, self.X):
            L = range( max(0, i-1), min(self.X, i+2) )
            for j in range(0, self.Y):
                s = 0
                live = ((i,j) in self.state)
                for k in range( max(0, j-1), min(self.Y, j+2) ):
                    for l in L:
                        if (l, k) in self.state:
                            s += 1
                s -= live
                #print(d)
                #print(i, j, s, live)
                if s == 3:
                    # Birth
                    d[(i,j)] = None
                elif s == 2 and live: 
                    # Survival
                    d[(i,j)] = self.state[(i,j)]
                elif live:
                    # Death
                    pass

        self.state = d

    def makeRandom(self):
        "Fill the board with a random pattern"
        self.erase()
        for i in range(0, self.X):
            for j in range(0, self.Y):
                if random.random() > 0.5:
                    self.set(i, j)

    #
    # Display-related methods
    #                    
    def draw(self, x, y):
        "Update the cell (x,y) on the display."
        turtle.penup()
        turtle.setpos(x*CELL_SIZE, y*CELL_SIZE)
        key = (x,y)
        if key in self.state:
            turtle.color('black')

            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE)
                turtle.right(90)
            turtle.end_fill()
            
    def display(self):
        """Draw the whole board"""
        turtle.clear()
        for i in range(0, self.X):
            for j in range(0, self.Y):
                self.draw(i, j)
        turtle.update()


def display_menu(stdscr, menu_y):
    "Display the menu of possible keystroke commands"
    erase_menu(stdscr, menu_y)
    stdscr.addstr(menu_y, 4,
                  'Use the cursor keys to move, and space or Enter to toggle a cell.')
    stdscr.addstr(menu_y+1, 4,
                  'E)rase the board, R)andom fill, S)tep once or C)ontinuously, Q)uit')

def keyloop(stdscr):
    # Clear the screen and display the menu of keys
    stdscr.clear()
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    menu_y = (stdscr_y-3)-1
    display_menu(stdscr, menu_y)

    # Allocate a subwindow for the Life board and create the board object
    subwin = stdscr.subwin(stdscr_y-3, stdscr_x, 0, 0)
    board = LifeBoard(subwin, char=ord('*'))
    board.display(update_board=False)

    # xpos, ypos are the cursor's position
    xpos, ypos = board.X//2, board.Y//2

    # Main loop:
    while (1):
        stdscr.move(1+ypos, 1+xpos)     # Move the cursor
        c = stdscr.getch()                # Get a keystroke
        if 0<c<256:
            c = chr(c)
            if c in ' \n':
                board.toggle(ypos, xpos)
            elif c in 'Cc':
                erase_menu(stdscr, menu_y)
                stdscr.addstr(menu_y, 6, ' Hit any key to stop continuously '
                              'updating the screen.')
                stdscr.refresh()
                # Activate nodelay mode; getch() will return -1
                # if no keystroke is available, instead of waiting.
                stdscr.nodelay(1)
                while (1):
                    c = stdscr.getch()
                    if c != -1:
                        break
                    stdscr.addstr(0,0, '/')
                    stdscr.refresh()
                    board.display()
                    stdscr.addstr(0,0, '+')
                    stdscr.refresh()

                stdscr.nodelay(0)       # Disable nodelay mode
                display_menu(stdscr, menu_y)

            elif c in 'Ee':
                board.erase()
            elif c in 'Qq':
                break
            elif c in 'Rr':
                board.makeRandom()
                board.display(update_board=False)
            elif c in 'Ss':
                board.display()
            else: pass                  # Ignore incorrect keys
        elif c == curses.KEY_UP and ypos>0:            ypos -= 1
        elif c == curses.KEY_DOWN and ypos<board.Y-1:  ypos += 1
        elif c == curses.KEY_LEFT and xpos>0:          xpos -= 1
        elif c == curses.KEY_RIGHT and xpos<board.X-1: xpos += 1
        else:
            # Ignore incorrect keys
            pass


def main():
    scr = turtle.Screen()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.shape('circle')
    turtle.shapesize(1, 1, 0)

    xsize, ysize = scr.screensize()
    board = LifeBoard(xsize // CELL_SIZE, ysize // CELL_SIZE)
    board.set(3, 5)
    board.set(4, 5)
    board.set(5, 5)
    board.makeRandom()
    board.display()
    while True:
        board.step()
        board.display()

if __name__ == '__main__':
    main()
