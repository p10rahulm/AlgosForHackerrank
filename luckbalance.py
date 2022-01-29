#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # print("k",k,"contests",contests)
    lb = 0
    newarray = []
    for i in range(len(contests)):
        if (contests[i][1] == 0):
            lb += contests[i][0]
        else:
            newarray.append(contests[i][0])
    newarray = sorted(newarray, reverse=True)
    if not newarray:
        return lb
    print("newarray=",newarray,"k=",k,"len(newarray)",len(newarray))
    for i in range(min(k,len(newarray))):
        lb += newarray[i]
    for i in range(k, len(newarray)):
        lb -= newarray[i]
    return lb


if __name__ == '__main__':
    file1 = open("input/input2.txt", "r")
    s = file1.readlines()
    first_multiple_input = s[0].rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    contests = []

    for i in range(n):
        contests.append(list(map(int, s[i+1].rstrip().split())))
    print("contests",contests)
    lb=luckBalance(k, contests)
    file1.close()
    print(lb)

