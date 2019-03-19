from recursion import sum_array, fibonacci, factorial, reverse
from sorting import bubble_sort, merge_sort, quick_sort

def test_sum_array():
    """
    test the correctness of sum_array
    """

    assert sum_array([1, 2, 3, 4]) == 10, 'incorrect'
    assert sum_array([1, -7, 3, 4]) == 1, 'incorrect'

def test_fibonacci():
    """
    test the function fibonacci(n)
    """

    assert fibonacci(9) == 34, 'incorrect'
    assert fibonacci(6) == 8, 'incorrect'

def test_factorial(n):
    """
    test the correctness of factorial(n)
    """

    assert factorial(9) == 362880, 'incorrect'
    assert factorial(0) == 1, 'incorrect'

def test_reverse():
    """Test the correctness of function reverse(word)"""

    assert reverse('string') == 'gnirts', 'incorrect'
    assert reverse('aobakwe') == 'ewkaboa', 'incorrect'

def test_bubble_sort():

    """Test the correctness of the function bubble_sort"""

    assert bubble_sort([38, 27, 43, 22, 3, 9, 82, 10]) == [3, 9, 10, 22, 27, 38, 43, 82], 'incorrect'
    assert bubble_sort([1, 6, 4, 3, 7, 34, 9]) == [1, 3, 4, 6, 7, 9, 34], 'incorrect'

def test_merge_sort():

    """Test the correctness of the function merge_sort"""

    assert merge_sort([38, 27, 43, 22, 3, 9, 82, 10]) == [3, 9, 10, 22, 27, 38, 43, 82], 'incorrect'
    assert merge_sort([1, 6, 4, 3, 7, 34, 9]) == [1, 3, 4, 6, 7, 9, 34], 'incorrect'

def test_quick_sort():

    """Test the correctness of the function quick_sort"""

    assert quick_sort([38, 27, 43, 22, 3, 9, 82, 10]) == [3, 9, 10, 22, 27, 38, 43, 82], 'incorrect'
    assert quick_sort([1, 6, 4, 3, 7, 34, 9]) == [1, 3, 4, 6, 7, 9, 34], 'incorrect'
