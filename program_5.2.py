#!/usr/local/bin/python3.6
"""Created on 2020-01-31
by Jibin Joseph

Assignment 02 - Building Complex Prorgams from Smaller Parts
Think Python Chapter 5: Exercise 5.2.

Function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.

Modified to add comments
"""

def check_fermat(a,b,c,n):
    """
    Fermat's Last Theorem
    Function takes 4 inputs and check whether Fermat's Last Theorem is valid

    a,b,c : Positive integers
    n: Any value greater than n
    """
    ## Uses "and" operator to combine the conditionals
    ## Conditional 1: n should be greater than 2
    ## Conditional 2: a^n + b^n =c^n
    if n>2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
        print("Fermat's Theorem is violated")
        return
    else:
        print("No, that doesn't work. ")
        print("Fermat's Theorem is not violated")


## Prompts user to input positive integers and coverts the string to integer
a=int(input("Enter a positive integer for a:\n" ))
b=int(input("Enter a positive integer for b:\n" ))
c=int(input("Enter a positive integer for c:\n" ))

## Use while and break to enforce the user to input n greater than 2
while True:
    n=int(input("Enter a value for n greater than 2:\n" ))
    if n>2:
        break
    print("Value is less than or equal to 2. Please enter a value greater than 2")

check_fermat(a,b,c,n)