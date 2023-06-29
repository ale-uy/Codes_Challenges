#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0.0
    neg = 0.0
    zer = 0.0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg +=1
        else:
            zer += 1
    
    pos = pos/len(arr)
    print(f"{pos:.6f}")
    neg = neg/len(arr)
    print(f"{neg:.6f}")
    zer = zer/len(arr)
    print(f"{zer:.6f}")
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
