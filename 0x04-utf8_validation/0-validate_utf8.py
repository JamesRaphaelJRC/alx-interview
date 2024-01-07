#!/usr/bin/python3
''' Defines a function validateUTF8 '''


def validUTF8(data):
    ''' etermines if a given data set represents a valid UTF-8 encoding '''
    # Variable to keep track of the number of consecutive leading bits
    leading_bits_count = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if leading_bits_count > 0:
            if (byte >> 6) == 0b10:
                # Decrease the count of remaining leading bits
                leading_bits_count -= 1
            else:
                # If it's not a continuation byte, return False
                return False
        else:
            # Count the number of leading bits in the current byte
            while (byte >> 7 - leading_bits_count) & 1 == 1:
                leading_bits_count += 1

            # Handle special cases
            if leading_bits_count == 1 or leading_bits_count > 4:
                return False

            # If it's a single-byte character, no need to check further
            if leading_bits_count == 0:
                continue

        # Decrement the count of remaining leading bits
        leading_bits_count -= 1

    # If there are remaining leading bits, it's an incomplete sequence
    return leading_bits_count == 0
