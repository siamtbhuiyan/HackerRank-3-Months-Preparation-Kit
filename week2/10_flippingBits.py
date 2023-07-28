#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary = '{:032b}'.format(n)
    inverted_str = ''

    for char in binary:
        if char == '0':
            inverted_str += '1'
        if char == '1':
            inverted_str += '0'

    integer = int(inverted_str, 2)
    return integer
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        print(result)