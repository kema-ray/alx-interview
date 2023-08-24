#!/usr/bin/python3
"""
Module that contains a method that determines if a given set of
data is valid for UTF-8 encoding.
"""

def validUTF8(data):
    """
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integer
    """

    number_of_bytes = 0
    mask = 255  # 11111111 in binary (8 bits)

    for num in data:
        """Checks if the first bit is a 0"""
        if number_of_bytes == 0:
            num  = num  & mask
            if (num >> 5) == 0b110:
                number_of_bytes = 1
            elif (num  >> 4) == 0b1110:
                number_of_bytes = 2
            elif (num  >> 3) == 0b11110:
                number_of_bytes = 3
            elif (num  >> 7):
                return False
        else:
            if (num  >> 6) != 0b10:
                return False
            number_of_bytes -= 1

    return number_of_bytes == 0 
