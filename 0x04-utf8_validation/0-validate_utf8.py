#!/usr/bin/python3
"""
Validate if a given list of integers 
represents a valid UTF-8 encoded string.
Each integer represents a byte (0-255).
"""

def validUTF8(data):
    num_bytes = 0  # Number of expected continuation bytes

    for byte in data:
        # Check if byte is within valid range (0-255)
        if byte < 0 or byte > 255:
            return False

        # If no continuation bytes are expected, identify the type of byte
        if num_bytes == 0:
            # Check lead byte to determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # If it starts with '1' but isn't a valid lead byte
                return False
        else:
            # Continuation byte check: should start with '10'
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are unfulfilled continuation bytes, it's invalid
    return num_bytes == 0
