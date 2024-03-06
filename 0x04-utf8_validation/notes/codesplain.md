#!/usr/bin/python3
""" Module for UTF-8 Validation"""



```
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
```

This implementation iterates over each byte in the given dataset and performs the following checks:

1. If `num_bytes_to_follow` is 0, it checks the first few bits of the current byte to determine the number of bytes that should follow.

2. If `num_bytes_to_follow` is not 0, it checks if the current byte is a continuation byte (i.e., starts with `10` in binary).

3. If any of the checks fail, it returns False immediately.

4. After iterating over all the bytes, it checks if all the bytes have been consumed by ensuring that `num_bytes_to_follow` is 0.

If all the checks pass, the method returns True, indicating that the given dataset represents a valid UTF-8 encoding. Otherwise, it returns False.
