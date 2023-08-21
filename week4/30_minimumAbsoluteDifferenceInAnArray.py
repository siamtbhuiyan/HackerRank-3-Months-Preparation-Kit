#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    minD = 1000000001
    for index in range(len(arr)):
        if index + 1 != len(arr):
            if abs(arr[index + 1] - arr[index]) < minD:
                minD = abs(arr[index + 1] - arr[index])
    return minD
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
