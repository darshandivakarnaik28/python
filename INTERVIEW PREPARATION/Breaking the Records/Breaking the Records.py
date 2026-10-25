#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    best=scores[0]
    worst=scores[0]
    best_count=0
    worst_count=0
    result=[]
    for i in range(1,len(scores)):
        if scores[i]>best:
            best=scores[i]
            best_count+=1
        if scores[i]<worst:
            worst=scores[i]
            worst_count+=1
    result.append(best_count)
    result.append(worst_count)
    return(result)     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
