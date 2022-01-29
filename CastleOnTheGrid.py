#!/bin/python3

import math
import os
import random
import re
import sys
import queue


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#
def createGraphAdjList(grid):
    n = len(grid)
    adjList = [[] for i in range(n ** 2)]
    gridBlocksMatrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        elemI = list(grid[i])
        for j in range(len(elemI)):
            gridBlocksMatrix[i][j] = 1 if elemI[j] == 'X' else 0

    # for i in range(n):
    #     print(i,"\t:\t",gridBlocksMatrix[i])
    for elemIndex in range(n ** 2):
        thisRow = elemIndex // n
        thisCol = elemIndex % n
        # Column Ahead
        i = 1
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisCol + i < n and not xHit):
            if (gridBlocksMatrix[thisRow][thisCol + i] == 0):
                adjList[elemIndex].append(thisRow * n + thisCol + i)
            else:
                xHit = 1
            i += 1
        # Columns Behind
        i = 1
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisCol - i > -1 and not xHit):
            if (gridBlocksMatrix[thisRow][thisCol - i] == 0):
                adjList[elemIndex].append(thisRow * n + thisCol - i)

            else:
                xHit = 1
            i += 1
        # Rows Ahead
        i = 1
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisRow + i < n and not xHit):
            if (gridBlocksMatrix[thisRow + i][thisCol] == 0):
                adjList[elemIndex].append((thisRow + i) * n + thisCol)
            else:
                xHit = 1
            i += 1

        # Rows Behind
        i = 1
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisRow - i > -1 and not xHit):
            if (gridBlocksMatrix[thisRow - i][thisCol] == 0):
                adjList[elemIndex].append((thisRow - i) * n + thisCol)

            else:
                xHit = 1
            i += 1
    '''
    for i in range(len(adjList)):
        print("row,col: %d,%d:\t"%(i//n,i%n),end='')
        for j in adjList[i]:
            print("(%d,%d)"%(j//n,j%n),end='')
        print("\n")
    '''
    return adjList


def createGraphAdjMatrix(grid):
    n = len(grid)
    adjMatrix = [[0 for i in range(n ** 2)] for j in range(n ** 2)]
    gridBlocksMatrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        elemI = list(grid[i])
        for j in range(len(elemI)):
            gridBlocksMatrix[i][j] = 1 if elemI[j] == 'X' else 0

    print("gridBlocksMatrix", gridBlocksMatrix)
    for elemIndex in range(n ** 2):
        thisRow = elemIndex // n
        thisCol = elemIndex % n
        # Column Ahead
        i = 0
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisCol + i < n and not xHit):
            if (gridBlocksMatrix[thisRow][thisCol + i] == 0):
                adjMatrix[elemIndex][thisRow * n + thisCol + i] = 1
            else:
                xHit = 1
            i += 1
        # Columns Behind
        i = 0
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisCol - i > -1 and not xHit):
            if (gridBlocksMatrix[thisRow][thisCol - i] == 0):
                adjMatrix[elemIndex][thisRow * n + thisCol - i] = 1
            else:
                xHit = 1
            i += 1
        # Rows Ahead
        i = 0
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisRow + i < n and not xHit):
            if (gridBlocksMatrix[thisRow + i][thisCol] == 0):
                adjMatrix[elemIndex][(thisRow + i) * n + thisCol] = 1
            else:
                xHit = 1
            i += 1

        # Rows Behind
        i = 0
        xHit = gridBlocksMatrix[thisRow][thisCol]
        while (thisRow - i > -1 and not xHit):
            if (gridBlocksMatrix[thisRow - i][thisCol] == 0):
                adjMatrix[elemIndex][(thisRow - i) * n + thisCol] = 1
            else:
                xHit = 1
            i += 1
    # print("adjMatrix",adjMatrix)
    return adjMatrix


def bfsdistance(adjList, numnodes, startNode, goalNode):
    n= numnodes
    visited = [0 for i in range(n ** 2)]
    distance = [0 for i in range(n ** 2)]
    q = []
    currNode = startNode
    for AdjNode in adjList[currNode]:
        if not visited[AdjNode]:
            distance[AdjNode]=1
            q.append(AdjNode)

    while (distance[goalNode] == 0):
        currNode=q.pop(0)
        if(visited[currNode]):
            # print("visitedNode",currNode)
            continue
        visited[currNode] = 1
        # print("currnode=(%d,%d)"%(currNode//n,currNode%n),"distance[currNode]",distance[currNode])
        for adjacentNode in adjList[currNode]:
            if not visited[adjacentNode]:
                distance[adjacentNode] = distance[currNode] + 1 if distance[adjacentNode]==0 else distance[adjacentNode]
                q.append(adjacentNode)
                # print("adjnode:(%d,%d)"%(adjacentNode//n,adjacentNode%n),"distance[adjacentNode]",distance[adjacentNode])


    return distance[goalNode]


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    # print("grid",grid)
    adjList = createGraphAdjList(grid)
    n = len(grid)
    startNode = startX * n + startY
    goalNode = goalX * n + goalY
    distance = bfsdistance(adjList, n, startNode, goalNode)

    return distance


if __name__ == '__main__':
    file1 = open("input/castle.txt", "r")
    s = file1.readlines()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(s[0].strip())

    grid = []

    for i in range(n):
        grid_item = s[i+1].rstrip()
        grid.append(grid_item)

    first_multiple_input = s[n+1].rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])
    '''
    print("first_multiple_input",first_multiple_input)
    print("grid", grid)
    for i in range(len(grid)):
        print(i,":", grid[i])
    '''
    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print("\nNumber of moves\t:\t",str(result) + '\n')

    file1.close()
