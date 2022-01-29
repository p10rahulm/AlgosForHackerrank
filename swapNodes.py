#!/bin/python3

import math
import os
import random
import re
import sys


class node:
    def __init__(self, label, parent, child1, child2, level):
        self.label = label
        self.parent = parent
        self.child1 = child1
        self.child2 = child2
        self.level = level
        self.visited = False


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#


def constructTree(indexes):
    nodes = []
    for i in range(len(indexes)):
        nodeElem = node(i + 1, -1, indexes[i][0], indexes[i][1], 1)
        nodes.append(nodeElem)
    for i in range(len(indexes)):
        if (indexes[i][0] != -1):
            nodes[indexes[i][0] - 1].parent = i + 1
            nodes[indexes[i][0] - 1].level = nodes[i].level + 1
        if (indexes[i][1] != -1):
            nodes[indexes[i][1] - 1].parent = i + 1
            nodes[indexes[i][1] - 1].level = nodes[i].level + 1
    # for i in range(len(nodes)):
    #     print("nodes[i].label", nodes[i].label, "nodes[i].parent", nodes[i].parent, "nodes[i].child1", nodes[i].child1,
    #           "nodes[i].child2", nodes[i].child2, "nodes[i].level", nodes[i].level)
    return nodes


def inorderTraverseOld(nodes, index, outstring):
    if index == -1:
        return outstring
    node = nodes[index - 1]
    # print("here with index",index,"outstring=",outstring)
    leftchildindex = node.child1
    rightchildindex = node.child2
    outstring = inorderTraverse(nodes, leftchildindex, outstring)
    # print("here with index mid1",index,"outstring=",outstring)
    outstring += ' ' + str(node.label)
    # print("here with index mid2",index,"outstring=",outstring,"rightchildindex=",rightchildindex)
    outstring = inorderTraverse(nodes, rightchildindex, outstring)
    # print("here with index end",index,"outstring=",outstring)
    return outstring

def inorderTraverseRecursive(nodes, index, outstring):
    if index == -1:
        return outstring
    node = nodes[index - 1]
    # print("here with index",index,"outstring=",outstring)
    leftchildindex = node.child1
    rightchildindex = node.child2
    outstring = inorderTraverse(nodes, leftchildindex, outstring)
    # print("here with index mid1",index,"outstring=",outstring)
    outstring += ' ' + str(node.label)
    # print("here with index mid2",index,"outstring=",outstring,"rightchildindex=",rightchildindex)
    outstring = inorderTraverse(nodes, rightchildindex, outstring)
    # print("here with index end",index,"outstring=",outstring)
    return outstring

def inorderTraverse(nodes, index, outstring):
    outstring=''
    for node in nodes:
        node.visited=False
    # i = 0
    while (True):
        if index==-1:
            break
        # i+=1
        # print("inside:%d,index=%d"%(i,index))
        node = nodes[index-1]
        # print("nodes[i].label", node.label, "nodes[i].parent", node.parent, "nodes[i].child1", node.child1,
        #                 "nodes[i].child2",node.child2, "nodes[i].level", node.level)

        leftChild = None
        rightChild = None
        if(node.child1!=-1):
            leftChild = nodes[node.child1-1]
        if (node.child2 != -1):
            rightChild = nodes[node.child2-1]
        # print("node.child1=",node.child1,"node.child2",node.child2)
        if(not leftChild and not rightChild):
            # print("in 1")
            outstring += ' ' + str(node.label)
            index = node.parent
            node.visited = True
            continue
        if(leftChild and leftChild.visited==False):
            # print("in 2")
            index = leftChild.label
            continue
        if ((not leftChild or (leftChild and leftChild.visited == True)) and not rightChild):
            # print("in 3")
            outstring += ' ' + str(node.label)
            index = node.parent
            node.visited = True
            continue
        if ((not leftChild or (leftChild and leftChild.visited == True)) and rightChild and rightChild.visited==True):
            # print("in 4")
            index = node.parent
            node.visited=True
            continue
        if ((not leftChild or (leftChild and leftChild.visited == True))  and rightChild and rightChild.visited==False):
            # print("in 5")
            outstring += ' ' + str(node.label)
            index = rightChild.label
            continue
    for node in nodes:
        node.visited=False
    return outstring


def swapNodes(indexes, queries):
    # Write your code here
    nodes = constructTree(indexes)
    outArray = []
    print("queries=",queries)
    for k in queries:
        outStr = ''
        for node in nodes:
            if (node.level % k == 0):
                temp = node.child1
                node.child1 = node.child2
                node.child2 = temp
        outStr = inorderTraverse(nodes, 1, outStr)
        print("k=",k,"outStr=", outStr)
        outArray.append(outStr.strip())

    # return ['312','213']
    return outArray
    # print("indexes",indexes)
    # print("queries",queries)
    # return 'abcd'


if __name__ == '__main__':
    file1 = open("input/input3.txt", "r")
    s = file1.readlines()
    first_multiple_input = s[0].rstrip()
    n = int(s[0].rstrip())
    print("n=",n)
    indexes = []

    for i in range(1,n+1):
        indexes.append(list(map(int, s[i].rstrip().split())))

    queries_count = int(s[n+1].rstrip().strip())

    queries = []

    for i in range(n+2,len(s)):
        queries_item = int(s[i].strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    # print(result)
    file1.close()


