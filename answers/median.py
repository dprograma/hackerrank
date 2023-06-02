#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # sort the array 'arr'
    arr = sorted(arr)
    # get the number of elements in array arr
    n = len(arr)

    mid = math.floor(n/2) + 1

    res = arr[mid-1]

    return res


if __name__ == '__main__':
    fptr = open('/Users/dprograma/hackerrank/answer', 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()