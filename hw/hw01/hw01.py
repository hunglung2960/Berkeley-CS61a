from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
    """ # learning: understand the constraint here and try to find the possible way.
                    # think about if I miss out some concept that's why I cannot do it
    """

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return (min(x,y,z))**2+(sorted([x,y,z])[1])**2

    """  # problem-solving flow
    # smallest^2+second_smallest^2
    # (min(x,y,z))**2+(sorted([x,y,z])[1])**2 """

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    k = 1
    answer = 1
    while n/k !=1:
        k = k+1
        if n%k==0 and k!=n:
            answer = k
    return answer

    """ 
    # Learning of problem-solving techniques:
    # while loop is for determining the range of operation you want to run through
    # if is like a gate to suck in the relevant value for returning from function.
    # use simple example to help think about what conditions to impose


    # problem-solving flow
    # generate a list of factors
        # smaller than n -
         #  k = 1
         #  while n/k != 1:
         #       k = k+1
         #       n = n/k
         #  return k
        # evenly divide n
    # pick the largest one - max() """




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
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function() 
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func()) 

""" # there should be something unique about taking in cond() through call to if_function()
# Learning: after return, no more evaluation will be executed. It just returns whatever there is.
# a function is indeed evaluated, but by typing it in terminal, nothing will return.
# so only the 2nd and 3rd argument is displayed """

def cond(): # return boolean value
    "*** YOUR CODE HERE ***"
    return False # in if condition, 1 return True. 

def true_func(): # return print()
    "*** YOUR CODE HERE ***"
    return print(42)

def false_func(): # return print()
    "*** YOUR CODE HERE ***"
    return print(47)






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
    "*** YOUR CODE HERE ***"
    length = 1
    print(int(n)) # so that it will also print the first one
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
        length = length + 1
        print(int(n)) # to print the subsequent values
    return length