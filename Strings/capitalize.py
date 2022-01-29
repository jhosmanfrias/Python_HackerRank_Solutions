#!/bin/python3

import math
import os
import random
import re
import sys
###########################################################################################
# Challenge -> https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true #
# Warning.  -> Put in your terminal this: export OUTPUT_PATH=/tmp/output.csv before       #
# By        -> jhosmanfrias, Jan-202                                                      #
###########################################################################################

# Complete the solve function below.
def solve(s):
    sf = ""
    for x in range(len(s)):
        if s[x] == " ":
            sf += s[x]
        else:
            if s[x-1] == " " or (x == 0 and s[x] != " "):
                sf += s[x].upper()
            else:
                sf += s[x]
    return sf

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

