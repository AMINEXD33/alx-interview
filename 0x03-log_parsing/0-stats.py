#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def output(lg: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(lg["file_size"]))
    for code in sorted(lg["code_frequency"]):
        if lg["code_frequency"][code]:
            print("{}: {}".format(code, lg["code_frequency"][code]))


if __name__ == "__main__":
    damn = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    lg = {}
    lg["file_size"] = 0
    lg["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = damn.fullmatch(line)
            if (match):
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                lg["file_size"] += file_size

                # status code
                if (code.isdecimal()):
                    lg["code_frequency"][code] += 1

                if (line_count % 10 == 0):
                    output(lg)
    finally:
        output(lg)