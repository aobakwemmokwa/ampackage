"""
Created on Mon Mar 18 14:25:07 2019

@author: Aobakwe Mmokwa
"""

def sum_array(array):

    """
    Calculate and return the sum of elements of a list

    Args:
        array (list): A list which's elements we return a sum of

    returns:
        the sum of elements of list (array) (int or float)

    """

    if array:        #if list is NOT empty
        return array[0] + sum_array(array[1:])      #recurcively splice the 1st element
    else:
        return 0


def fibonacci(n):

    """
    Compute the nth value of the fibonacci sequence

        fibonacci sequence: f(n) = f(n-1) + f(n+2)
        f(0) = 0, f(1) = 1, f(2) = 1 ...

    Args:
        n (int): The number of the fibonacci value to return

    Returns:
        given n return f(n) (int)

    """

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    """
    Compute the factorial of n (n!)
        n! = n x (n-1) x (n-2) x ... x 1

    Args:
        n (int): The number for which we want a factorial for

    returns:
        n factorial (int)
    """

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    """
    Given a string, return the string in reverse order
        given 'string' return 'gnirts'

    Args:
        word (str): A string to reverse

    returns
        (str): word in reverse order
    """

    if word:
        return word[-1] + reverse(word[:-1])
    else:
        return ''
