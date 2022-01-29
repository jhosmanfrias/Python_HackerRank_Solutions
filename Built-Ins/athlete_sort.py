#!/bin/python3
#################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                           #
#################################################################################################

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    def takeK (elem):
        return elem [k]
    
    arr.sort(key = takeK)
    
    for i in range(n):
        for j in range(m):
            print (arr[i][j], end= " ")
        print ("")

