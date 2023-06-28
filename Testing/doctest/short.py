from doctest import testmod
def add(a,b):
    '''
    Given two integers, return the sum.
    :param a: int
    :param b: int
    :return: int

    >>> add(2,3)
    5
    '''
    return a + b 

testmod(name='add', verbose = True)