#!/usr/bin/python3
''' Defines a function validateUTF8 '''
from typing import List


def validUTF8(data: List[int]) -> bool:
    ''' Determines if a given data set represents a valid UTF-8 encoding '''
    try:
        leading_bits_count = 0

        # Masks for checking if byte is valid (Starts with 10)
        mask_1 = 1 << 7
        mask_2 = 1 << 6

        for byte in data:

            mask_n_byte = 1 << 7

            if leading_bits_count == 0:
                # Count number of bytes the UTF-8 Character will have
                while mask_n_byte & byte:
                    leading_bits_count += 1
                    mask_n_byte = mask_n_byte >> 1

                # If number of bytes did not increase then it has 1 byte
                # which is the same we are counting so no need to check
                # next bytes for current character
                if leading_bits_count == 0:
                    continue

                # A character in UTF-8 can be 1 to 4 bytes long
                # But 1 byte characters start in 0 so leading_bits_count
                # should never be 1
                if leading_bits_count == 1 or leading_bits_count > 4:
                    return False

            else:
                # Every byte that is not the first byte of a character
                # should start with 10, otherwise is not valid
                if not (byte & mask_1 and not (byte & mask_2)):
                    return False

            # If bytes of character are valid, then the count will
            # decrease with each byte until a new character starts
            leading_bits_count -= 1

        # All characters were verified correctly with their proper
        # byte count
        return leading_bits_count == 0
    except TypeError as e:
        return False
