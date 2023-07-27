# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

inputList = []

while True:
    try:
        inp = input().rstrip()
        inputList.append(inp)
    except:
        break
    

for string in inputList:
    if string[0] == 'S' and string[2] == 'M':
        string = string[4:-2]
        strings = re.split("([A-Z][^A-Z]*)", string)
        strings = [s for s in strings if s]
        strings = [s.lower() for s in strings]
        string = " ".join(strings)
        print(string)
    elif string[0] == 'S' and string[2] == 'C':
        string = string[4:]
        strings = re.split("([A-Z][^A-Z]*)", string)
        strings = [s for s in strings if s]
        strings = [s.lower() for s in strings]
        string = " ".join(strings)
        print(string)
    elif string[0] == 'S' and string[2] == 'V':
        string = string[4:]
        strings = re.split("([A-Z][^A-Z]*)", string)
        strings = [s for s in strings if s]
        strings = [s.lower() for s in strings]
        string = " ".join(strings)
        print(string)
    elif string[0] == 'C' and string[2] == 'M':
        string = string[4:]
        strings = string.split()
        string = strings[0]
        strings = [s.title() for ind, s in enumerate(strings) if ind != 0]
        string = string + "".join(strings) + "()"
        print(string)
    elif string[0] == 'C' and string[2] == 'C':
        string = string[4:]
        strings = string.split()
        strings = [s.title() for s in strings]
        string = "".join(strings)
        print(string)
    elif string[0] == 'C' and string[2] == 'V':
        string = string[4:]
        strings = string.split()
        string = strings[0]
        strings = [s.title() for ind, s in enumerate(strings) if ind != 0]
        string = string + "".join(strings)
        print(string)
