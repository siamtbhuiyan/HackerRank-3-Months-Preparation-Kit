#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    half = int(math.floor(n / 2))
    print(n)
    
    if p <= half:
        print(int(math.floor(p / 2)))
        return int(math.floor(p / 2))
    else:
        if n - p == 1 and n % 2 == 0:
            return 1
        else:
            return int(math.floor((n - p) / 2))

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
