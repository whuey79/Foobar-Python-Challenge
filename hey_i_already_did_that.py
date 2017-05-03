"""
Level 2.1: Hey, I Already Did That!
========================
Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 
You have worked out that the algorithm has the following process: 
1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2
For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.
Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.
Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function answer(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, answer(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (string) n = "1211"
    (int) b = 10
Output:
    (int) 1
Inputs:
    (string) n = "210022"
    (int) b = 3
Output:
    (int) 3
"""

def answer(n, b):
    """
    Find the length of the cycle, given a number n, and base b
    :param n: starting n
    :type n:  string
    :param b:  base of number n
    :type b:  int
    :return:  length of cycle
    :rtype:  int
    """
    # track previous numbers seen
    previous_numbers = []

    # keep appending numbers until we get find a cycle
    while n not in previous_numbers:
        previous_numbers.append(n)
        n = get_next_minion(n, b)

    # find the index of the number
    index_of_num = previous_numbers.index(n)

    # if index matches the last value in the list, return 1
    if index_of_num == len(previous_numbers)-1:
        return 1

    # return len of cycle
    return len(previous_numbers[index_of_num:])


def get_next_minion(n, b):
    """
    Returns number after it's been manipulated (z = x - y), where x, y derived by n
    :param n current number n, in a given base
    :type n: str
    :param b: base of number n
    :type b: int
    :return: new number z
    :rtype: int
    """

    """
    :parm b (int) base to work with
    """
    # get the length of n
    k = len(n)

    # convert to list to get x and y
    list_n = list(n)

    # create str_x, based off values of n in DESC order
    str_x = ''.join(sorted(list_n, key=int, reverse=True))
    # create str_x, based off values of n in ASC order
    str_y = reverse_string(str_x)

    # convert to ints to base10 to do math
    x = int(str_x, b)
    y = int(str_y, b)
    z = x - y

    # convert base10 int back to original b
    z = base10ToX(z, b)
    z = str(z)

    # pad z to len k
    while len(z) < k:
        z = '0' + z
    return str(z)


def base10ToX(num, base):
    """
    Converts a number from base 10 to new base
    :param num: number to convert
    :type num: int
    :param base: base to convert to
    :type base: int
    :return: number in new base
    :rtype: int
    """
    if num < base:
        return num % base

    stack = []

    while num >= base:
        rem = num % base
        stack.append(str(rem))
        num = num / base

    if num > 0:
        stack.append(str(num))
    val = reverse_string(''.join(stack))

    return int(val)

def reverse_string(x):
    """
    reverses a string
    :param x: string to reverse
    :type x: str
    :return: reversed string
    :rtype: str
    """
    return x[::-1]
