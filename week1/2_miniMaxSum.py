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
    maxSum = 0
    minSum = 9999999999999999999999999999
    sums = [
        arr[0] + arr[1] + arr[2] + arr[3],
        arr[0] + arr[2] + arr[3] + arr[4],
        arr[0] + arr[1] + arr[3] + arr[4],
        arr[0] + arr[1] + arr[2] + arr[4],
        arr[1] + arr[2] + arr[3] + arr[4]
    ]
    
    for s in sums:
        if s > maxSum:
            maxSum = s
        if s < minSum:
            minSum = s
    
    print(minSum, maxSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
