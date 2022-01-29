#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid2(s):
    # Write your code here
    sCounter = Counter()
    for letter in s:
        sCounter[letter] += 1


    modeCounter = Counter()

    for key in sCounter:
        modeCounter[sCounter[key]] += 1
    print("sCounter", sCounter)
    print("modeCounter", modeCounter)

    numGreaterThan1 = 0
    diffinKeys = 0
    for index, key in enumerate(modeCounter):
        diffinKeys += math.pow(-1, index) * key
        if modeCounter[key] > 1:
            numGreaterThan1 += 1
    print("modeCounter", modeCounter)
    print("diffinKeys", diffinKeys)
    if (numGreaterThan1 > 1 or len(modeCounter) > 2 or abs(diffinKeys) > 1):
        return "NO"

    return "YES"


def isValid(s):
    # Write your code here
    sCounter = Counter()
    for letter in s:
        sCounter[letter] += 1
    sCounterBase = [0 for keys in sCounter]
    modeCounter = Counter()

    for key in sCounter:
        modeCounter[sCounter[key]] += 1
    print("modeCounter", modeCounter)
    if (len(modeCounter) ==1):
        return "YES"
    if(len(modeCounter)>2):
        return "NO"
    modeKeys = list(modeCounter.keys())
    modeVals = []
    for i in range(len(modeKeys)):
        modeVals.append(modeCounter[modeKeys[i]])
    if(1 not in modeVals):
        return "NO"
    if (modeCounter[1]==1  or abs(modeKeys[0]-modeKeys[1])<=1):
        return "YES"
    return "NO"


if __name__ == '__main__':
    file1 = open("input/input.txt", "r")
    s = file1.readline()
    file1.close()
    result = isValid(s)
    print("result=",result)
    result = isValid("aaaaabc")
    print("result=", result)
