#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    roundedGrades = []
    
    for grade in grades:
        if grade % 5 == 3 and grade > 37:
            roundedGrades.append(grade + 2)
        elif grade % 5 == 4 and grade > 37:
            roundedGrades.append(grade + 1)
        else:
            roundedGrades.append(grade)
    
    return roundedGrades
            
if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
