#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    hasNum = 1
    hasLow = 1
    hasUpp = 1
    hasSp = 1    
    
    for char in password:
        if char in numbers:
            hasNum = 0
        if char in lower_case:
            hasLow = 0
        if char in upper_case:
            hasUpp = 0
        if char in special_characters:
            hasSp = 0
            
    eNum = hasNum + hasLow + hasUpp + hasSp

    if n < 6:
        num = 6 - n
    else:
        num = 0
    
    if eNum > num:
        num = num + (eNum - num)
        
    return num

if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
