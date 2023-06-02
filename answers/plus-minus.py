import math
import os
import random
import re
import sys


def plusMinus(arr):
    n = len(arr)
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1

    print("{:.6f}".format(pos_count/n))
    print("{:.6f}".format(neg_count/n))
    print("{:.6f}".format(zero_count/n))

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
