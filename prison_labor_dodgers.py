"""
Level 1: Prison Labor Dodgers
====================
Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!
Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function answer(x, y) that compares the lists and returns the additional ID.
For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function answer(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function answer(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.
In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int list) x = [13, 5, 6, 2, 5]
    (int list) y = [5, 2, 5, 13]
Output:
    (int) 6
Inputs:
    (int list) x = [14, 27, 1, 4, 2, 50, 3, 1]
    (int list) y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
Output:
    (int) -4
Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

def diff_list(x, y):
    '''
    Answer to https://www.google.com/url?q=https%3A%2F%2Fgist.github.com%2Fwill-tr%2F98ae9374365dde4df8e05d2bef41b4cd&sa=D&sntz=1&usg=AFQjCNHldGahlIEQMess5Ohi-bz8IDmb9w
    
    Given 2 arrays of matching elements (except for 1), find the differing element
    :param x: array 1 with values -1000 to 1000
    :param y: array 1 with values -1000 to 1000
    :return: 
    '''
    d = {}
    diff = None
    # //
    if len(x) > len(y):
        # x is larger
        smaller_array = y
        larger_array = x
    else:
        # y is larger
        smaller_array = x
        larger_array = y
    # create counter of what's seen
    for item in smaller_array:
        d[item] = 1
    # check against counter and return val
    for item in larger_array:
        if item not in d:
            diff = item
            break
    return diff


"""
Test cases:
11
x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]
10
x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
01
x = [-1,1]
y = [-1]
00
x = [-1,-12]
y = [-1]
"""
