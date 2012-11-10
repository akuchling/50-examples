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

import sys
import turtle
import random

CELL_SIZE = 10                  # Measured in pixels

class LifeBoard:
    """Encapsulates a Life board

    Attributes:
    xsize, ysize : horizontal and vertical size of the board
    state : set containing (x,y) coordinates for live cells.

    Methods:
    display(update_board) -- Display the state of the board on-screen.
    erase() -- clear the entire board
    makeRandom() -- fill the board randomly
    set(x,y) -- set the given cell to Live; doesn't refresh the screen
    toggle(x,y) -- change the given cell from live to dead, or vice
                   versa, and refresh the screen display

    """
    def __init__(self, xsize, ysize):
        """Create a new LifeBoard instance.

        scr -- curses screen object to use for display
        char -- character used to render live cells (default: '*')
        """
        self.state = set()
        self.xsize, self.ysize = xsize, ysize

    def is_legal(self, x, y):
        "Returns true if the x,y coordinates are legal for this board."
        return (0 <= x < self.xsize) and (0 <= y < self.ysize)

    def set(self, x, y):
        """Set a cell to the live state."""
        if not self.is_legal(x, y):
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                    x, y, self.xsize, self.ysize))
                             
        key = (x, y)
        self.state.add(key)

    def makeRandom(self):
        "Fill the board with a random pattern"
        self.erase()
        for i in range(0, self.xsize):
            for j in range(0, self.ysize):
                if random.random() > 0.5:
                    self.set(i, j)

    def toggle(self, x, y):
        """Toggle a cell's state between live and dead."""
        if not self.is_legal(x, y):
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                    x, y, self.xsize, self.ysize))
        key = (x, y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def erase(self):
        """Clear the entire board."""
        self.state.clear()

    def step(self):
        "Compute one generation, updating the display."
        d = set()
        for i in range(self.xsize):
            x_range = range( max(0, i-1), min(self.xsize, i+2) )
            for j in range(self.ysize):
                s = 0
                live = ((i,j) in self.state)
                for yp in range( max(0, j-1), min(self.ysize, j+2) ):
                    for xp in x_range:
                        if (xp, yp) in self.state:
                            s += 1

                # Subtract the central cell's value; it doesn't count.
                s -= live             
                ##print(d)
                ##print(i, j, s, live)
                if s == 3:
                    # Birth
                    d.add((i,j))
                elif s == 2 and live: 
                    # Survival
                    d.add((i,j))
                elif live:
                    # Death
                    pass

        self.state = d

    #
    # Display-related methods
    #                    
    def draw(self, x, y):
        "Update the cell (x,y) on the display."
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x*CELL_SIZE, y*CELL_SIZE)
            turtle.color('black')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE-1)
                turtle.left(90)
            turtle.end_fill()
            
    def display(self):
        """Draw the whole board"""
        turtle.clear()
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.draw(i, j)
        turtle.update()


def display_help_window():
    from turtle import TK
    root = TK.Tk()
    frame = TK.Frame()
    canvas = TK.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    help_screen = turtle.TurtleScreen(canvas)
    help_t = turtle.RawTurtle(help_screen)
    help_t.penup()
    help_t.hideturtle()
    help_t.speed('fastest')

    width, height = help_screen.screensize()
    line_height = 20
    y = height // 2 - 30
    for s in ("Click on cells to make them alive or dead.",
              "Keyboard commands:",
              " E)rase the board",
              " R)andom fill",
              " S)tep once or",
              " C)ontinuously -- use 'S' to resume stepping",
              " Q)uit"):
        help_t.setpos(-(width / 2), y)
        help_t.write(s, font=('sans-serif', 14, 'normal'))
        y -= line_height
    

def main():
    display_help_window()

    scr = turtle.Screen()
    turtle.mode('standard')
    xsize, ysize = scr.screensize()
    turtle.setworldcoordinates(0, 0, xsize, ysize)

    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    board = LifeBoard(xsize // CELL_SIZE, 1 + ysize // CELL_SIZE)

    # Set up mouse bindings
    def toggle(x, y):
        cell_x = x // CELL_SIZE
        cell_y = y // CELL_SIZE
        if board.is_legal(cell_x, cell_y):
            board.toggle(cell_x, cell_y)
            board.display()

    turtle.onscreenclick(turtle.listen)
    turtle.onscreenclick(toggle)

    board.makeRandom()
    board.display()

    # Set up key bindings
    def erase():
        board.erase()
        board.display()
    turtle.onkey(erase, 'e')

    def makeRandom():
        board.makeRandom()
        board.display()
    turtle.onkey(makeRandom, 'r')

    turtle.onkey(sys.exit, 'q')

    # Set up keys for performing generation steps, either one-at-a-time or not.
    continuous = False
    def step_once():
        nonlocal continuous
        continuous = False
        perform_step()

    def step_continuous():
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():
        board.step()
        board.display()
        # In continuous mode, we set a timer to display another generation
        # after 25 millisenconds.
        if continuous:
            turtle.ontimer(perform_step, 25)

    turtle.onkey(step_once, 's')
    turtle.onkey(step_continuous, 'c')

    # Enter the Tk main loop
    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()
