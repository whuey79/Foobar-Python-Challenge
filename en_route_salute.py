"""
Level 2.2: En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4
"""

def get_num_salutes(s):
    """
    Get total number of salutes from employees passing each other in string s
    
    Design:
    -Iterate through string and stop at occurrence of emp walking right '>'
    -Check from current index to string end and count occurrences of '<'
    -Increment salute counter by 2
    -Repeat until string is traversed

    :param employee_walk_string: string that denotes employee position and walk dir
    :type employee_walk_string: string
    :return: total number of salutes, 2 per passing
    :rtype: int
    """
    EMP_WALKING_LEFT = '<'
    EMP_WALKING_RIGHT = '>'
    num_salutes = 0

    for index, value in enumerate(s):
        if value == EMP_WALKING_RIGHT:
            remaining_walk_string = s[index:]
            num_salutes += remaining_walk_string.count(EMP_WALKING_LEFT)

    return num_salutes * 2
