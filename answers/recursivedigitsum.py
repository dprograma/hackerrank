#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Base case: if n has only 1 digit, return n
    if len(n) == 1:
        return int(n)
    
    # Calculate the sum of the digits in n
    digit_sum = sum(int(digit) for digit in n)
    
    # Multiply the sum by k
    digit_sum *= k
    
    # Convert the sum back to a string and recursively call superDigit
    return superDigit(str(digit_sum), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
