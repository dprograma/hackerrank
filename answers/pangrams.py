#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Convert the string to lowercase to ignore case
    s = s.lower()
    
    # Create a set of all alphabets in the English language
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    
    # Iterate through each character in the string
    for char in s:
        # If the character is an alphabet, remove it from the set
        if char in alphabets:
            alphabets.remove(char)
    
    # If the set is empty, then the string is a pangram
    if not alphabets:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
