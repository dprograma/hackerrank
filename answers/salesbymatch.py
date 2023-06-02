#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # initialize a dictionary to store the frequency of each element
    freq = {}
    
    # initialize the sum of the items with frequency up to 2 
    total = 0    
    
    # loop through the array and update the frequency dictionary
    for item in ar:
        if item in freq:
            freq[item] += 1
            if freq[item] % 2 == 0:
                total += 1    
        else:
            freq[item] = 1
            
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()