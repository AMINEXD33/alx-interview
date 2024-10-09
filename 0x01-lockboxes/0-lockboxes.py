#!/usr/bin/python3
"""a module that contains a function that solves the problem Lockboxes"""


def canUnlockAll(boxes):
    """
    function that takes an array of boxes that may or
    may not contain keys to other boxes
    and determins if all boxes can be oppened
    """
    count = 1
    cach = {}
    for box_index in range(len(boxes)):

        for key in boxes[box_index]:
            if key == box_index:
                count += 1
            else:
                # cache the key
                cach[key] = True

        if cach.get(box_index):
            count += 1
    if count == len(boxes):
        return True
    return False
