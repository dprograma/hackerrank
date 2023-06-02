#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def lonelyinteger(a):
    # Initialize a dictionary to store the frequency of each element
    freq = {}
    
    # Loop through the array and update the frequency dictionary
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    # Loop through the frequency dictionary and return the element with frequency 1
    for key, value in freq.items():
        if value == 1:
            return key
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
