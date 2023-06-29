#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    m = 0 if s[-2:] == "AM" else 12
    aux = s.split(":")
    if aux[0] == "12":
        if m == 0:
            aux[0] = "00"
        else:
            aux[0] = "12"
    else:
        aux[0] = str(int(aux[0])+m)
        if len(aux[0]) < 2:
            aux[0] = "0" + aux[0]
    return f"{aux[0]}:{aux[1]}:{aux[2][:-2]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
