#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # create a list of alphabets
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # create a shifted alphabet by rotating the original alphabet
    shifted_alphabet = alphabet[k%26:] + alphabet[:k%26]
    # create a dictionary that maps each alphabet to its shifted alphabet
    mapping = dict(zip(alphabet, shifted_alphabet))
    # create a variable to store the encrypted string
    encrypted_string = ""
    # loop through each character in the input string
    for char in s:
        # if the character is a letter, encrypt it using the mapping dictionary
        if char.isalpha():
            encrypted_string += mapping[char.lower()].upper() if char.isupper() else mapping[char]
        # if the character is not a letter, leave it unchanged
        else:
            encrypted_string += char
    return encrypted_string


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = '/Users/dprograma/hackerrank/questions/answer.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
