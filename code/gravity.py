#!/usr/bin/env python3

import math
from turtle import *

# The gravitational constant G
G = 6.67428e-11

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
SCALE = 100 / AU

class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body.

    Extra attributes:
    mass : mass in kg
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """
    
    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0
    
    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)

        # Report an error if the distance is zero; otherwise we'll
        # get a ZeroDivisionError exception further down.
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        # Compute the force of attraction
        f = G * self.mass * other.mass / (d**2)

        # Compute the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def update_info(step):
    """(Turtle, int)
    
    Displays information about the status of the simulation.
    """
    tt = Turtle()
    tt.hideturtle()
    tt.color('black', 'white')

    # Clear the information area by drawing a square.
    tt.penup()
    tt.goto(-200,200)
    tt.pendown()
    tt.setheading(0)
    tt.begin_fill()
    for i in range(4):
        tt.forward(50) ; tt.right(90)
    tt.end_fill()

    # Display information
    tt.penup()
    tt.goto(-190, 180)
    tt.write('Step {0}'.format(step),
                      font=("Arial", 16, "normal"))

def loop(bodies):
    """([Body])

    Returns 
    """
    timestep = 24*3600  # One day
    
    for body in bodies:
        body.penup()
        body.hideturtle()

    step = 1
    while True:
        update_info(step)
        step += 1

        force = {}
        for body in bodies:
            totalx = totaly = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                totalx += fx
                totaly += fy

            force[body] = (totalx, totaly)

        # Update velocities
        for body in bodies:
            fx, fy = force[body]
            print(body.name)
            print('Starting vel.    =', body.vx, body.vy)
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
            print('Vel. after step  =', body.vx, body.vy)
            print()

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)


def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    sun.pencolor('yellow')

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec
    earth.pencolor('blue')

    #random = Body()
    #random.name = 'Random'
    #random.mass = 10**20
    #random.px = -.5*AU
    #random.vy = -35 * 1000
    #random.vx = 1000

    loop([sun, earth])

if __name__ == '__main__':
    main()
