#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    e=""
    for i,char in enumerate(s):
        if i==0 or s[i-1]==" ":
            if char.isalpha():
                e+=char.title()
            else:
                e+=char
        elif char==" ":
            e+=" "
        else:
            e+=char
    return "".join(e)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
