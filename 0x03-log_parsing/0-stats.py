#!/usr/bin/python3
""" this module contains a functions that can parse some data :> """
import re
import fileinput
import sys


def output(log: dict, fileSize: int) -> None:
    """
    helper function to display stats
    """
    print(f"File size: {fileSize}")
    for key in log:
        print(f"{key}: {log[key]}")


def create_dict_of_respose_codes() -> dict:
    """
    helper function that initiate a dict with the wanted response codes
    """
    res_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    dict_: dict = {}
    for key in res_codes:
        dict_[key] = 0
    return dict_


def isValidResponse(code: int) -> bool:
    """
    helper function that checks if a response code is valid
    (what we want , ignoring others)
    """
    if code in [200, 301, 400, 401, 403, 404, 405, 500]:
        return True
    return False


if __name__ == "__main__":
    damn = r'^([0-9]*\.[0-9]*)*\s-\s(\[[0-9]{4}-[0-9]{2}-[0-9]{2}\s)(:?[0-9]{2}:?)*\.([0-9]*\])\s("[A-Z]*)\s(\/[a-zA-Z0-9]*(\/?[a-zA-Z0-9]*))\s(HTTP\/[0-9]{1}\.[0-9]")\s([0-9]{3})\s([0-9]*)'  # nopep8

    responses_dict: dict = create_dict_of_respose_codes()
    file_size: int = 0
    iterations: int = 0
    try:
        for line in sys.stdin:
            rgx = re.search(damn, line)
            if rgx:
                iterations += 1
                code: int = int(rgx.group(9))
                if isValidResponse(code):
                    responses_dict[code] = responses_dict[code] + 1
                pass
                try:
                    file_size += int(rgx.group(10))
                except Exception:
                    pass
                if iterations % 10 == 0:
                    output(responses_dict, file_size)
    finally:
        output(responses_dict, file_size)
