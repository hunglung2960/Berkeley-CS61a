"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes): # Learning: *outcomes unpack a list or tuple into position arguments
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index # declare that we use nonlocal index, that is, the index just bef def dice()
        index = (index + 1) % len(outcomes)
        return outcomes[index] # learning: because of nonlocal the index does not restart?
    return dice 


# env diagram: 
# http://pythontutor.com/visualize.html#code=%0Adef%20make_test_dice%28*outcomes%29%3A%20%23%20Learning%3A%20*outcomes%20unpack%20a%20list%20or%20tuple%20into%20position%20arguments%0A%20%20%20%20%22%22%22Return%20a%20die%20that%20cycles%20deterministically%20through%20OUTCOMES.%0A%0A%20%20%20%20%3E%3E%3E%20dice%20%3D%20make_test_dice%281,%202,%203%29%0A%20%20%20%20%3E%3E%3E%20dice%28%29%0A%20%20%20%201%0A%20%20%20%20%3E%3E%3E%20dice%28%29%0A%20%20%20%202%0A%20%20%20%20%3E%3E%3E%20dice%28%29%0A%20%20%20%203%0A%20%20%20%20%3E%3E%3E%20dice%28%29%0A%20%20%20%201%0A%20%20%20%20%3E%3E%3E%20dice%28%29%0A%20%20%20%202%0A%0A%20%20%20%20This%20function%20uses%20Python%20syntax/techniques%20not%20yet%20covered%20in%20this%20course.%0A%20%20%20%20The%20best%20way%20to%20understand%20it%20is%20by%20reading%20the%20documentation%20and%20examples.%0A%20%20%20%20%22%22%22%0A%20%20%20%20assert%20len%28outcomes%29%20%3E%200,%20'You%20must%20supply%20outcomes%20to%20make_test_dice'%0A%20%20%20%20for%20o%20in%20outcomes%3A%0A%20%20%20%20%20%20%20%20assert%20type%28o%29%20%3D%3D%20int%20and%20o%20%3E%3D%201,%20'Outcome%20is%20not%20a%20positive%20integer'%0A%20%20%20%20index%20%3D%20len%28outcomes%29%20-%201%0A%20%20%20%20def%20dice%28%29%3A%0A%20%20%20%20%20%20%20%20nonlocal%20index%20%23%20declare%20that%20we%20use%20nonlocal%20index,%20that%20is,%20the%20index%20just%20bef%20def%20dice%28%29%0A%20%20%20%20%20%20%20%20index%20%3D%20%28index%20%2B%201%29%20%25%20len%28outcomes%29%0A%20%20%20%20%20%20%20%20return%20outcomes%5Bindex%5D%20%23%20learning%3A%20because%20of%20nonlocal%20the%20index%20does%20not%20restart%3F%0A%20%20%20%20return%20dice%20%0A%20%20%20%20%0Adice%20%3D%20make_test_dice%281,2,3%29%0Adice%28%29%0Adice%28%29%0Adice%28%29%0Adice%28%29&cumulative=false&curInstr=29&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


