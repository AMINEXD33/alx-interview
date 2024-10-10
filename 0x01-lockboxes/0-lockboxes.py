#!/usr/bin/python3
"""a module that contains a function that solves the problem Lockboxes"""


def valid_box(boxes, jump_index):
    """
    check if a box is a valid box to check
    """
    if jump_index > len(boxes) - 1 or jump_index < 0:
        return False
    return True


def canUnlockAll(boxes):
    """
    function that takes an array of boxes that may or
    may not contain keys to other boxes
    and determines if all boxes can be opened.
    """
    curr_box = 0
    found_keys = [0]
    already_opened = {0: True}
    count = 1

    while found_keys:
        curr_box = found_keys.pop(0)
        for key in boxes[curr_box]:
            if key != curr_box and key not in already_opened:
                found_keys.append(key)
                already_opened[key] = True
                count += 1

        if count == len(boxes):
            return True

    return count == len(boxes)
