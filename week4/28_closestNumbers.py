#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    """
    ### SLOW IMPLEMENTATION
    arr = sorted(arr)
    length = len(arr)
    resArr = []
    minD = 10000001
    for index1, elem1 in enumerate(arr):
        for index2 in range(index1 + 1, length):
            if arr[index2] - elem1 == minD:
                resArr.append(elem1)
                resArr.append(arr[index2])
            elif arr[index2] - elem1 < minD:
                minD = arr[index2] - elem1
                resArr = []
                resArr.append(elem1)
                resArr.append(arr[index2])
    """
    ### FAST IMPLEMENTATION
    arr = sorted(arr)
    length = len(arr)
    resArr = []
    minD = 10000001
    for index in range(0, length):
        if index + 1 != length:
            if arr[index + 1] - arr[index] == minD:
                resArr.append(arr[index])
                resArr.append(arr[index + 1])
            elif arr[index + 1] - arr[index] < minD:
                minD = arr[index + 1] - arr[index]
                resArr = []
                resArr.append(arr[index])
                resArr.append(arr[index + 1])
            
    return resArr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)
