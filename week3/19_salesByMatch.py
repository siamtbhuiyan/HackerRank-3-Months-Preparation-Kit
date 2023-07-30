#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = 0
    checked = []
    for index1, i in enumerate(ar):
        temp_count = 0
        for index2, j in enumerate(ar):
            if i not in checked:
                if i == j:
                    temp_count += 1
                if temp_count == 2:
                    print(i)
                    count += 1
                    temp_count = 0
        checked.append(i)
    return count
                
                
if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
