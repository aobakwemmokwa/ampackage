#ampackage
This package is created by Aobakwe Mmokwa as an exercise to learn how to create
a pip installable library using atom text editor and github.

The package has two modules, namely, recursion and sorting

recursion has the following functions:
  sum_array(array) which returns sum of elements of an sum_array
  factorial(n) which returns the factorial of a given number
  reverse(word) which return the given word in reverse order
  fibonacci(n) which returns the nth number in the fibonacci sequence

  all functions are written using recursion.

sorting has the the following functions:
  merge_sort, bubble_sort, quick_sort each function takes a list of integers
  and return a sorted list of the given elements.
  Each using the name case method as defined in Mathematics.

##building this package locally
  `python setup.py sdist`

##installing from github
  `pip install git+https://github.com/--------------`

##updating this package from github
  `pip install --upgrade git+https://github.com/--------------`
