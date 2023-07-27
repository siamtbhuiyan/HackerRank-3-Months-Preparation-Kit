#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    maxScore = -1
    minScore = 999999999999999999999999
    maxCount = -1
    minCount = -1

    for s in scores:
        if s < minScore:
            minScore = s
            minCount += 1
        if s > maxScore:
            maxScore = s
            maxCount += 1
    
    return [maxCount, minCount]
    
if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
