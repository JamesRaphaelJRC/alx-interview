#!/usr/bin/python3
''' The Pascals triangle '''


def pascal_triangle(n):
    ''' Defines the Pascal triangle

        n = Size of the pascal triangle
        pascal = A list of list of integers
        sublist_idx = The index of the previous sub-list of the pascal list
                    initial value = -1 since there is no previous sub-list yet
        prev = index of the previous value in the sublist_idx list
        current = index of the current value in the sublist_idx list
    '''
    if type(n) != int or n <= 0:
        return []

    pascal = []
    sublist_idx = -1
    for i in range(1, n + 1):
        new = []
        for j in range(i):
            try:
                current = j
                prev = current - 1
                if prev < 0:
                    prev = 0
                    val = 1
                else:
                    val = pascal[sublist_idx][prev] + pascal[sublist_idx][current]
            except IndexError:
                val = 1
            new.append(val)
        pascal.append(new)
        sublist_idx += 1
    return pascal
