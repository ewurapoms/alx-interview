#!/usr/bin/ python3
"""utf validation module"""


def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The list of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes_to_follow = 0

    for num in data:
        # Check if the current byte is the start of a new character
        if num_bytes_to_follow == 0:
            # Count the number of bytes to follow based on the first few bits
            if num >> 7 == 0b0:
                num_bytes_to_follow = 0
            elif num >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif num >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if num >> 6 != 0b10:
                return False

            num_bytes_to_follow -= 1

    # Check if all the bytes have been consumed
    return num_bytes_to_follow == 0
