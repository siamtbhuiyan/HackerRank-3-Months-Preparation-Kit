#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counting_list = [0]*6
    for i in arr:
        counting_list[i] += 1
    
    max_type_count = 0
    max_type = 0
    for index, i in enumerate(counting_list):
        if i > max_type_count:
            max_type_count = i
            max_type = index
    
    return max_type

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
