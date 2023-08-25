#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr = sorted(arr)
    length = len(arr)
    minUnfairness = 1000000001
    for i in range(k - 1, length):
        if arr[i] - arr[i - (k-1)] < minUnfairness:
            minUnfairness = arr[i] - arr[i - (k-1)]
        
    return minUnfairness
        
if __name__ == '__main__':
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
