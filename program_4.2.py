#!/usr/local/bin/python3.6
"""Created on 2020-01-31
by Jibin Joseph

Modified to add comments
"""

## Required packages
import turtle
import math

jibin = turtle.Turtle()

def polyline(t, n, length, angle):
    """
    Functions draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments

    Functions called: polyline

    fd indicates forward
    lt indicates left turn
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """
    Functions draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees

    Functions called: polyline

    lt indicates left turn
    rt indicates right turn
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """
    Function draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs

    Functions called: arc

    lt indicates left turn
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """
    Function draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs

    Functions called: petal

    lt indicates left turn
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """
    Functions moves Turtle (t) forward (length in pixel) units without leaving a trail.
    t: turtle
    length: distance to be moved

    method pu stands for “pen up”
    method pd stands for “pen down”.
    """
    t.pu()
    t.fd(length)
    t.pd()


## Main Code

move(jibin, -200)
## Draw turtle flowers with 7 petals with radius of 60 pixels with arc angle of 60 degree
## If angle subtended by arc is equal to 60 deg, it will cause no gap between petals
flower(jibin, 7, 60.0, 60.0)

move(jibin, 200)
## Draw turtle flowers with 10 petals with radius of 40 pixels with arc angle of 80 degree
## As angle subtended by arc is greater than 36 deg , it will causes petals to overlap
flower(jibin, 10, 40.0, 80.0)

move(jibin, 200)
## Draw turtle flowers with 20 petals with radius of 140 pixels with arc angle of 20 degree
## As angle subtended by arc is greater than 18 deg , there will be a small gap between petals
flower(jibin, 20, 140.0, 20.0)

## Hides the turtle at end
jibin.hideturtle()
turtle.mainloop()