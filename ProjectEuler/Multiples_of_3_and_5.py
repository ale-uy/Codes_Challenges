#!/bin/python3

import sys

    
def from_math(n):
    return  3*(n//3)*(n//3+1)//2 + 5*(n//5)*(n//5+1)//2 - 15*(n//15)*(n//15+1)//2
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(from_math(n-1))
