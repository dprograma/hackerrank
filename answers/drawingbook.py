#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Calculate the number of pages to turn to from the front
    front_turns = p // 2
    
    # Calculate the number of pages to turn to from the back
    back_turns = (n // 2) - (p // 2)
    
    # Calculate the minimum number of pages to turn
    return min(front_turns, back_turns)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
