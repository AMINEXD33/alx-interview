#!/usr/bin/python3
"""a module that contains a function that solves the problem Lockboxes"""


def canUnlockAll(boxes):
    """
    function that takes an array of boxes that may or
    may not contain keys to other boxes
    and determines if all boxes can be opened.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
