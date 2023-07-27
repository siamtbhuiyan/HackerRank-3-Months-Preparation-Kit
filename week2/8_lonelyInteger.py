#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    lonelyInt = 101
    for i in a:
        temp = 0
        for j in a:
            if i == j:
                temp += 1
        if temp < 2:
            lonelyInt = i
    
    return lonelyInt

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)
