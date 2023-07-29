#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    result = 0
    n = int(len(matrix) / 2)
    start1 = 0
    end1 = len(matrix) - 1
    for i in range(n):
        start2 = 0
        end2 = len(matrix) - 1
        for j in range(n):
            temp_arr = []
            temp_arr.append(matrix[start1][start2])
            temp_arr.append(matrix[start1][end2])
            temp_arr.append(matrix[end1][start2])
            temp_arr.append(matrix[end1][end2])
            result += max(temp_arr)
            start2 += 1
            end2 -= 1
        start1 += 1
        end1 -= 1
    return result
            
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)
