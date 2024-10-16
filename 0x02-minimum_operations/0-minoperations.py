#!/usr/bin/python3
"""this module contains three function to
help solve the Minimum Operations problem"""


def past(n, current_value, copied_value):
    """
    simulate a past , by returning the copied value
    and the current value
    """
    calc = current_value + copied_value
    return calc


def deapth_search(n, operation=1, current_value=1, copied_value=0, ops=0):
    """
    a recursive function that can search for the least possible
    operation(copy past) we can do to reach a number n, if no
    possible operation count is found the function returns False
    """
    # we did a past
    if operation == 0:
        current_value = past(n, current_value, copied_value)
        ops += 1
        # we found a possible number of operations
        if current_value == n:
            return ops
        # we're off target
        elif current_value > n:
            return False
        """
        note that after every past there two possible cource of action
        an other past or a copy
        """
        # copy
        rs1 = deapth_search(n, 1, current_value, copied_value, ops)
        # past
        rs2 = deapth_search(n, 0, current_value, copied_value, ops)

        # if both cources of action return, check the smallest
        if rs1 is not False and rs2 is not False:
            if rs1 > rs2:
                return rs2
            else:
                return rs1
        # only one cource of action returns
        elif rs1:
            return rs1
        # only one cource of action returns
        elif rs2:
            return rs2
        # none retuned no possible answer was found
        else:
            return False

    # we did a copy
    elif operation == 1:
        if copied_value != current_value:
            copied_value = current_value
        ops += 1
        """
        for every copy only one posible action is possible and it's a past
        """
        rs1 = deapth_search(n, 0, current_value, copied_value, ops)
        # if the corce of action returned
        if rs1 is not False:
            return rs1
        # no answer was found
        else:
            return False


def minOperations(n):
    """this function returns the result of searching for the least amount
    of ops that could reach to n, otherwise return False
    """
    res = deapth_search(n)
    if res is False:
        return 0
    return res
