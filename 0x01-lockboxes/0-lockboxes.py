#!/usr/bin/python3
"""a module that contains a function that solves the problem Lockboxes"""


def canUnlockAll(boxes):
    """
    function that takes an array of boxes that may or
    may not contain keys to other boxes
    and determins if all boxes can be oppened
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False]
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < n and not unlocked[new_key]:
            unlocked[new_key] = True
            keys.update(boxes[new_key])
    return all(unlocked)