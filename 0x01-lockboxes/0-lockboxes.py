#!/usr/bin/python3
''' Defines a function 'canUnlockAll' '''


def canUnlockAll(boxes):
    ''' Returns True if all boxes can be opened and False otherwise '''
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
