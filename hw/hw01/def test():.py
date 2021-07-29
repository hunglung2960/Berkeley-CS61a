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
    length = 0
    print(n) # so that it will also print the first one
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
        length = length + 1
        print(n) # to print the subsequent values
    return length

# to ponder: why does the print within function will print?
# why hailstone(10) does not return length?

a=hailstone(10) # a = function that contains print() -> once a is bound to them -> print out. WHY?
print(a)