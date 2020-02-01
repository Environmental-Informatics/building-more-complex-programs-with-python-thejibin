#!/usr/local/bin/python3.6
"""Created on 2020-01-31
by Jibin Joseph

Assignment 02 - Building Complex Prorgams from Smaller Parts
Think Python Chapter 7: Exercise 7.1.

Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.

Modified to add comments
"""

## Import required packages
import math

def mysqrt(a):
    """
    Function calculates the square root of a number

    a: number
    """

    ## Choose reasonable value of x
    x=a/2

    epsilon=0.0000001

    while True:

        y = (x + a/x) / 2
        ## Initially, tried with epsilon,but was not geeting same values
        ## When changed to 0, obtained same value as table
        if abs(y-x) == 0:
            break
        x = y
    return x

## Main Code

## Define an empty list and add header rows
list=[]
list.append(['a','mysqrt(a)','math.sqrt(a)','diff'])
list.append(['-'*3,'-'*18, '-'*18,'-'*18])

## Calculates the four columns
for i in range(1,10):
    list.append([i,mysqrt(i),math.sqrt(i),abs(mysqrt(i)-math.sqrt(i))])

## Print the four columns
for j in range(0,i+2):
    print('{:<4s}{:<20s}{:<20s}{:<30s}'.format(str(list[j][0]), str(list[j][1]),str(list[j][2]),str(list[j][3])))
