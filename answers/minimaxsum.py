#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # sort the array in ascending order
    arr.sort()

    # calculate the minimum sum by summing the first four elements
    min_sum = sum(arr[:4])

    # calculate the maximum sum by summing the last four elements
    max_sum = sum(arr[-4:])

    # print the minimum and maximum sums as a single line of two space-separated long integers
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
