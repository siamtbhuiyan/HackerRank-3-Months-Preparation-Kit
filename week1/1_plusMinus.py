#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    length = len(arr)
    
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        else:
            zero += 1
    
    print("%.6f" % (positive/length))
    print("%.6f" % (negative/length))
    print("%.6f" % (zero/length))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
