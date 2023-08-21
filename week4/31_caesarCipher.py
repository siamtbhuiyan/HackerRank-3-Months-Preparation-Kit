#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lowStr = string.ascii_lowercase
    uppStr = string.ascii_uppercase
    newStr = ''
    if k > 26:
        k = k % 26
    for i in s:
        if i in lowStr:
            if lowStr.index(i) + k >= 26:
                newStr += lowStr[(lowStr.index(i) + k) - 26]
            else:
                newStr += lowStr[lowStr.index(i) + k]
        elif i in uppStr:
            if uppStr.index(i) + k >= 26:
                newStr += uppStr[(uppStr.index(i) + k) - 26]
            else:
                newStr += uppStr[uppStr.index(i) + k]
        else:
            newStr += i  
  
    return newStr

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
