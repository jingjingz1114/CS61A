from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub(a, b)
    else:
        f = add(a , b)
    return f

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if a>=b:
        largest = a
        smallest = b
    else:
        largest = b
        smallest =a

    if largest>=c:
        if c>=smallest:
            second_largest = c
        else:
            second_largest = smallest
    else:
        second_largest = largest
        largest = c
    result = largest**2 + second_largest**2
    return result

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    list = []
    for i in range(1,n):
        if n % i == 0:
            list.append(i)
    return max(list)







def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False
def t():
    "*** YOUR CODE HERE ***"
    return 0
def f():
    "*** YOUR CODE HERE ***"
    return 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    step = 1
    while n>=1:
        print(int(n))

        if n ==1:
            return step

        elif n % 2 == 0:
            n = n/2

        else:
            n = n * 3 +1
        step += 1
    return step
if __name__ == "__main__":
    import doctest
    doctest.testmod()


