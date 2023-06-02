#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])

    # sort each row of the grid in ascending alphabetical order
    for i in range(n_rows):
        grid[i] = sorted(grid[i])

    # check if the columns are also in ascending alphabetical order
    for j in range(n_cols):
        for i in range(n_rows-1):
            if grid[i][j] > grid[i+1][j]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()