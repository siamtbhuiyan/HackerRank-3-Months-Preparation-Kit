#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    zeros = [1]*26
    
    string = s.lower()
    
    for index, i in enumerate(string):
        if i in lowercase:
            zeros[lowercase.index(i)] = 0
                
    if 1 not in zeros:
        return 'pangram'
    else:
        return 'not pangram'
    

if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result)
