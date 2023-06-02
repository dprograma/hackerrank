#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # extract hour, minute, second, and AM/PM indicator
    hour, minute, second = map(int, s[:-2].split(':'))
    am_pm = s[-2:]
    
    # if time is 12:00AM, convert to 00:00:00
    if hour == 12 and am_pm == 'AM':
        hour = 0
    
    # if time is between 1:00AM and 11:59AM, keep the same hour
    elif am_pm == 'AM':
        hour = hour % 12
    
    # if time is 12:00PM, keep the same hour
    elif hour == 12 and am_pm == 'PM':
        pass
    
    # if time is between 1:00PM and 11:59PM, add 12 to the hour
    else:
        hour = (hour % 12) + 12
    
    # return formatted 24-hour time
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
