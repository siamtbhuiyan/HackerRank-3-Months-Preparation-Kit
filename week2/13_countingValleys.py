#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    position = 0
    count = 0
    for i in path:
        if i == 'U' and position == -1:
            count += 1
        if i == 'U':
            position += 1
        if i == 'D':
            position -= 1
    
    return count

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
