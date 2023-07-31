#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    longest = 0
    
    for i in a:
        temp_longest = 0
        for j in a:
            if i == j:
                temp_longest += 1
            elif i + 1:
                if i + 1 == j:
                    temp_longest += 1
        if temp_longest > longest:
            longest = temp_longest
    
    return longest
                               
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
