import math
import random

def squareParams(side):
    """
    Calculate the area, perimeter, and diagonal of a square.

    Args:
        side (float): The length of the side of the square.

    Returns:
        tuple: A tuple containing the area, perimeter, and diagonal.
    """
    area = side ** 2
    perimeter = 4 * side
    diagonal = math.sqrt(2) * side
    return area, perimeter, diagonal

def isNumberPrime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool or str: True if the number is prime, False otherwise. 
                     Returns a string if the number is out of range.
    """
    if num < 0 or num > 1000:
        return "Please enter a number between 0 and 1000"
    elif num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def randomList(N):
    """
    Generate a list of N random integers between -100 and 100.

    Args:
        N (int): The number of elements in the list.
    
    Returns:
        list: A list of N random integers.
    """
    if N < 0:
        return "Please enter a whole number greater than 0"
    else:
        return [random.randint(-100, 100) for _ in range(N)]

def listOfBiggerNumbers(num, lst):
    """
    Create a new list with all elements from the input list that are greater than the given number.
    
    Args:
        num (int): The number to compare against.
        lst (list): The list of numbers to filter.

    Returns:
        list: A new list containing elements greater than num.
    """
    if len(lst) == 0:
        return "Please enter a list of numbers"
    else:
        return [int(i) for i in lst if int(i) > num]
    
def amountOfSameNumbers(num, lst):
    """
    Count the occurrences of a number in a list.

    Args:
        num (int): The number to count.
        lst (list): The list of numbers.
    
    Returns:
        int: The count of occurrences of num in lst.
    """
    if len(lst) == 0:
        return "Please enter a list of numbers"
    else:
        return lst.count(num)

def listOfRepeatedNumbers(lst1, lst2):
    """
    Create a new list with all elements that are present in both input lists.

    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.
    
    Returns:
        list: A new list containing elements that are present in both lst1 and lst2.
    """
    if len(lst1) == 0 or len(lst2) == 0:
        return "Please enter two lists of numbers"
    else:
        return [i for i in lst1 if i in lst2]

def listOfUniqueElements(lst1, lst2):
    """
    Create a new list with all elements of the first list that don't appear in the second list.

    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.
    
    Returns:
        list: A new list containing elements from lst1 that are not in lst2.
    """
    if len(lst1) == 0 or len(lst2) == 0:
        return "Please enter two lists of numbers"
    else:
        return [i for i in lst1 if i not in lst2]