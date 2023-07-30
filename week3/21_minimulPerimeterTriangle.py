#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    new = [list(s) for s in set(itertools.combinations(sticks, 3))]
    for i in new:
        i.sort()

    possible = []
    
    for i in new:
        if i[0] + i[1] > i[2]:
            possible.append(i)
                
    if len(possible) > 1:
        maxP = 0
        maxI = -1
        for index, i in enumerate(possible):
            if sum(i) > maxP:
                maxP = sum(i)
                maxI = index
        return list(possible[maxI])
    elif len(possible) == 1:
        return list(possible[0])
    else:
        return [-1]

if __name__ == '__main__':
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(result)
