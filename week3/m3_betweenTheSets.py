#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    minV = min(min(a), min(b))
    maxV = max(max(a), max(b))
    
    count = 0
    
    for i in range(minV, maxV + 1):
        temp_count = 0
        for j in a:
            if i%j == 0:
                temp_count += 1
        for k in b:
            if k%i == 0:
                temp_count += 1
        
        if temp_count == (len(a) + len(b)):
            count += 1
            
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
