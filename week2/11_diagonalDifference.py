#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftSum = 0
    rightSum = 0
    
    for index, i in enumerate(arr):
        leftSum += i[index]
        rightSum += i[len(i) - index - 1]
        
    result = abs(leftSum - rightSum)
    return result
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)