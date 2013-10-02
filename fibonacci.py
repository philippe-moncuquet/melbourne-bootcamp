import math
import doctest

# recursive solution
def factorial(n):
    '''Returns the factorial value of the input
    
    F(N) = N * factorial(N-1)
    
    >>>factorial(0)
    1
    >>>factorial(1)
    1
    >>>factorial(2)
    2
    >>>factorial(8)
    40320
    '''
    # Exception example
    if not isinstance(n, int):
        raise Exception("Factorial must be feeded with integers")
    if n < 0:
        raise Exception("Factorial for negative numbers is undefined")
    assert n >= 0
    assert isinstance(n, int)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)





def fibonacci(n):
    '''Returns the Nth value in the Fibonacci sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, F(1) = 1
    
    >>>fibonacci(0)
    0
    >>>fibonacci(1)
    1
    >>>fibonacci(2)
    1
    >>>fibonacci(5)
    5
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a
    
    
# only run this block if we're
# executing this script directly;
# don't run if importing!
if __name__ == "__main__":
    doctest.testmod()


'''
# function testing
tests = [
         [0,0],
         [1,1],
         [2,1],
         [3,2],
         [5,5],
         ]
for input, expected_results in tests:
    assert fibonacci(input) == expected_results
'''
#assert fibonacci(0) == 0
#assert fibonacci(1) == 1
#assert fibonacci(2) == 1
#assert fibonacci(3) == 2
#assert fibonacci(5) == 5









