#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
     length = len(s)
     if length % 2 != 0:
        return -1
     startStr = s[:length // 2]
     endStr = s[length // 2:]
     numOp = 0
     for i in startStr:
        if i in endStr:
            endStr = endStr.replace(i, "", 1)
        else:
            numOp += 1
    
     return numOp

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
