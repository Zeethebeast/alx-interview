#!/usr/bin/python3
"""
Validate if a given list of integers 
represents a valid UTF-8 encoded string.
Each integer represents a byte (0-255).
"""

def validUTF8(data):
    num_byte = 0  # Number of continuation bytes expected

    for byte in data:
        # Ensure byte is within valid range (0-255)
        if byte < 0 or byte > 255:
            return False

        # If no continuation bytes are expected, determine the type of byte
        if num_byte == 0:
            # Determine the number of bytes in this UTF-8 character
            if byte >> 5 == 0b110:  # 2-byte character
                num_byte = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_byte = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_byte = 3
            elif byte >> 7:  # If top bit is 1 but it's not a valid lead byte
                return False
        else:
            # Check that continuation bytes start with '10'
            if byte >> 6 != 0b10:
                return False
            num_byte -= 1

    # If there are any expected continuation bytes left, it's an invalid encoding
    return num_byte == 0
