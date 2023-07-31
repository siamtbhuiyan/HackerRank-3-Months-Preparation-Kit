#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for i in range(int(len(s) / 2)):
        digits = s[:i + 1]
        s_num = int(s[:i + 1])
        num = s_num
        while len(digits) < len(s):
            num += 1
            digits += str(num)
        
        if digits == s:
            print("YES", s_num)
            return
    
    
    print("NO")
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
