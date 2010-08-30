#!/usr/bin/env python

import math
from turtle import *

# The gravitational constant G
G = 6.67e-11

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
    
    mass = None
    vx = vy = 0.0
    px = py = 0.0
    
    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
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
    sun.mass = 1.98892 * 10**30

    earth = Body()
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec

    loop([sun, earth])

def loop(bodies):
    """()
    """
    timestep = 24*3600  # One day
    
    for body in bodies:
        body.penup()

    while True:
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
            print body.vx, body.vy
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
            print body.vx, body.vy
            print

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot()


if __name__ == '__main__':
    main()
