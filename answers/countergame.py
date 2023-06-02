#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Initialize the player
    louise = True

    # Count the number of set bits in n-1
    bit_count = bin(n - 1).count('1')

    # Switch players based on the count of set bits
    louise = not (bit_count % 2 == 0)

    # Return the winner
    if louise:
        return 'Louise'
    else:
        return 'Richard'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
