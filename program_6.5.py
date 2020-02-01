#!/usr/local/bin/python3.6
"""Created on 2020-01-31
by Jibin Joseph

Assignment 02 - Building Complex Prorgams from Smaller Parts
Think Python Chapter 6: Exercise 6.5.

The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder. One way to find the GCD of two numbers is based
on the observation that if r is the remainder when a is divided by b, then
gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a. Write a function
called gcd that takes parameters a and b and returns their greatest common divisor.

Modified to add comments
"""

def gcd(a,b):
    """
    a,b: two integers

    r: remainder when a is divided by b
    """
    ## GCD is not defined for this case
    if a==0 and b==0:
        """
        Source: http://mfleck.cs.illinois.edu/building-blocks/version-1.0/number-theory.pdf
        It states that GCD is not defined for 0 and 0
        """
        return("not defined")

    ## Base case for iteration
    if a==0 or b==0:
        return (max(a,b))

    ## For swapping the integers if a is less than b
    if a<b:
        a,b=b,a

    r=a%b
    ## Calling gcd again (recursively)
    return gcd(b,r)

## Prompts the user to input a and b & also converts from string to integer
a=int(input("Enter a integer value of a:  \n"))
b=int(input("Enter a integer value of b: \n"))

## Print using format operator
## Converts value of gcd to accommodate GCD not defined
print("The greatest common divisor (GCD) of %d and %d is: %s" % (a, b, str(gcd(a,b))))