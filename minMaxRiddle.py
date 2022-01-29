#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the riddle function below.
def riddle(arr):
    # complete this function
    numLargestWindow = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        j = i + 1
        count = 0
        while (j < len(arr) and arr[j] >= arr[i]):
            j += 1
            count += 1
        j = i - 1
        while (j >= 0 and arr[j] >= arr[i]):
            j -= 1
            count += 1
        numLargestWindow[i] += count
    print("arr", arr)
    print("numLargestWindow",numLargestWindow)
    windowsForWhichNumHighest = {}
    for i in range(len(numLargestWindow)):
        if arr[i] not in windowsForWhichNumHighest:
            windowsForWhichNumHighest[arr[i]] = numLargestWindow[i]
        elif (numLargestWindow[i] >= windowsForWhichNumHighest[arr[i]]):
            windowsForWhichNumHighest[arr[i]] = numLargestWindow[i]
    print("\nwindowsForWhichNumHighest\n",windowsForWhichNumHighest)
    numGivenWindowSize = {}
    for item, window in windowsForWhichNumHighest.items():
        if window not in numGivenWindowSize:
            numGivenWindowSize[window] = item
        else:
            numGivenWindowSize[window] = max(item, numGivenWindowSize[window])
    print("\nnumGivenWindowSize\n",numGivenWindowSize)

    sortedWindowsSize = sorted(list(numGivenWindowSize.keys()), reverse=True)
    print("sortedWindowsSize",sortedWindowsSize)
    windowsForSortedWindowsSize = [0 for i in range(len(sortedWindowsSize))]
    for i in range(len(sortedWindowsSize)):
        windowsForSortedWindowsSize[i] = numGivenWindowSize[sortedWindowsSize[i]]
    print("windowsForSortedWindowsSize", windowsForSortedWindowsSize)
    for i in range(1,len(windowsForSortedWindowsSize)):
        if(windowsForSortedWindowsSize[i]<windowsForSortedWindowsSize[i-1]):
            windowsForSortedWindowsSize[i]= windowsForSortedWindowsSize[i-1]
    print("windowsForSortedWindowsSize", windowsForSortedWindowsSize)
    for i in range(1,len(windowsForSortedWindowsSize)):
        numGivenWindowSize[sortedWindowsSize[i]] = windowsForSortedWindowsSize[i]
    print("\nnumGivenWindowSize\n", numGivenWindowSize)
    sortedWindowsSize = sorted(list(numGivenWindowSize.keys()), reverse=True)
    print("sortedWindowsSize", sortedWindowsSize)

    outarray = [0 for i in range(len(arr))]
    for i in range(len(sortedWindowsSize)):
        # print("i=",i,"sortedWindowsSize[i]",sortedWindowsSize[i])
        if (i != len(sortedWindowsSize) - 1):
            # print("in1")
            for j in range(sortedWindowsSize[i], sortedWindowsSize[i + 1], -1):
                outarray[j - 1] = numGivenWindowSize[sortedWindowsSize[i]]
                # print("j=",j,"outarray[j]",outarray[j-1])
        else:
            # print("in 2")
            for j in range(sortedWindowsSize[i], 0, -1):
                outarray[j - 1] = numGivenWindowSize[sortedWindowsSize[i]]
                # print("j=",j,"outarray[j]",outarray[j-1])
    # print("outarray",outarray)
    return outarray


if __name__ == '__main__':
    file1 = open("input/input4.txt", "r")
    s = file1.readlines()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(s[0])

    arr = list(map(int, s[1].rstrip().split()))

    res = riddle(arr)

    print(' '.join(map(str, res)))
    print('\n')

    file1.close()
