#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer. If n is 0, returns 1 as 0! is 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve input from command-line arguments and calculate the factorial
if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please provide a valid integer as input.")
else:
    print("Usage: ./factorial_recursive.py <integer>")
