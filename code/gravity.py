#!/usr/bin/env python

import math
from turtle import *

# The gravitational constant G
G = 6.67e-11

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
SCALE = AU / 100.0

class Body(Turtle):
    mass = None
    vx = vy = 0.0

    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Compute the distance of the other body.
        sx, sy = self.position()
        ox, oy = other.position()
        dx = (ox-sx) * SCALE
        dy = (oy-sy) * SCALE
        r = math.sqrt(dx**2 + dy**2)

        # Compute the force of attraction
        f = G * self.mass * other.mass / (r**2)

        # Compute the direction
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def main():
    sun = Body()
    sun.mass = 1e49
    sun.penup()

    earth = Body()
    earth.mass = 1e36
    earth.penup()
    earth.goto(-100, 100)
    earth.vy = 35

    loop([sun, earth])

def loop(bodies):
    """()
    """
    while True:
        print 'loop'
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
            body.vx += fx / body.mass
            body.vy += fy / body.mass

            # Update positions
            bx, by = body.position()
            bx = (bx*SCALE + body.vx) / SCALE
            by = (by*SCALE + body.vy) / SCALE
            body.goto(bx, by)
            body.dot()



if __name__ == '__main__':
    main()
