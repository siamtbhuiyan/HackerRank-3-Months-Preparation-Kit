#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    start = 0
    end = m - 1
    
    while end < len(s):
        temp_sum = 0
        for i in range(start, end + 1):
            temp_sum += s[i]
            if i == end:
                if temp_sum == d:
                    count += 1
        start += 1
        end += 1
        
    return count

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
