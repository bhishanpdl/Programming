#!python

def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-3)
    90

    """
    return x*x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
