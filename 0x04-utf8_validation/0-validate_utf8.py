#!/usr/bin/python3
"""
Validate if a given list of integers 
represents a valid UTF-8 encoded string.
Each integer represents a byte (0-255).
"""

def validUTF8(data):
    num_byte = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        if byte < 0 or byte > 255:
            # Invalid byte found; return False immediately
            return False

        if num_byte == 0:
            mask = 1 << 7
            while mask & byte:
                num_byte += 1
                mask >>= 1

            if num_byte == 0:
                continue

            if num_byte == 1 or num_byte > 4:
                return False
        else:
            # Check if the byte starts with '10' in binary form
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_byte -= 1

    return num_byte == 0
