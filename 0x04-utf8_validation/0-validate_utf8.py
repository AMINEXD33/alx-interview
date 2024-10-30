#!/usr/bin/python3
"""this module contains a function that validate UTF-8"""
# def DETERMINE_ERROR(err):
#     print(err, end=" > ")


def validUTF8(data):
    def get_x_most_significant_bits(number: int, x: int):
        """
        get the str representation of the x most significan't bits
        of a number
        """
        return format(number, "#010b").removeprefix("0b")[:x]

    def expecting_a_sequence(mode: str, sequence_count: list[int, int]):
        """
        this function determines of we're expecting a byte that belongs to
        a sequence
        """
        if mode == "sequence" and sequence_count[0] != sequence_count[1]:
            return True
        return False

    def initiate_sequence_count():
        """
        this function initiat the count, by returning
        a list of two ints that represent [expected_count, current_count]
        """
        return [0, 0]

    def found_a_sequence(sequence_count: list[int, int]):
        """
        this function adds one to current_count and returns a new list
        """
        return [sequence_count[0], sequence_count[1] + 1]

    def how_many_expected_bytes(bits_repr: str):
        """
        this function determins how many bytes are we epecting
        to be part of the sequence
        """
        count = 0
        for bit in bits_repr:
            if bit == "1":
                count += 1
            elif bit == "0":
                break
        return count

    mode: str = "none"
    # first int is the lenght if the sequence,
    # the second is how many did we find
    sequence_count: list[int, int] = [0, 0]
    for char in data:
        if char > 255:  # not a valud byte
            # DETERMINE_ERROR("char is way bigger \
            # to fit in a byte making it unvalid")
            return False
        # check if it's just ascci
        char_repr: str = get_x_most_significant_bits(char, 4)
        if char_repr[0] == "0":
            # if we found an ascci and we're expecting a sequence
            # return False
            if expecting_a_sequence(mode=mode, sequence_count=sequence_count):
                # DETERMINE_ERROR("we found an ascci and we're \
                # expecting a sequence")
                return False
            mode = "ascci"
            continue  # don't do anything

        elif char_repr[0] == "1":
            # for example a leading 10xxxxxx wouldn't be expected at the start
            # befor finding a set up , like 110xxxxx
            if char_repr[:2] == "10" and mode != "sequence":
                # DETERMINE_ERROR(
                #     "we're not expecting a sequence, and this is a sequence"
                # )
                return False

            elif char_repr[:2] == "10" and mode == "sequence":
                # we found a sequence number update the count
                sequence_count = found_a_sequence(
                    sequence_count=sequence_count
                )
                # if we cound a sequence and it's out of range return False
                if sequence_count[1] > sequence_count[0]:
                    # DETERMINE_ERROR("we're out of range for this sequence")
                    return False

            elif char_repr[:2] == "11":
                # if we found a leading sequence and we're expecting a
                # sequence number
                # return False
                if expecting_a_sequence(
                    mode=mode, sequence_count=sequence_count
                ):
                    # DETERMINE_ERROR(
                    #     "we found a leading sequence and
                    # we're expecting a sequence number"
                    # )
                    return False

                # update the mode
                mode = "sequence"
                # initiate the sequence_count
                sequence_count = initiate_sequence_count()
                # we're expecting how many bytes
                expected_bytes = how_many_expected_bytes(char_repr)
                # update count
                # we're including this leading one
                sequence_count[0] = expected_bytes - 1
    # if we exited without finding all bytes in a sequence return False
    if sequence_count[0] != sequence_count[1]:
        # DETERMINE_ERROR("we're done travercing the
        # list but we couldn't find the rest of the sequence")
        return False
    return True
