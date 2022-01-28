#!/bin/python3
###########################################################################################
# Challenge -> https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                     #
###########################################################################################

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    
    text_not = "Not Weird"
    text = "Weird"
    
    modulo = n % 2
    
    #print (modulo)
    
    if modulo == 1:
        print (text)
    
    if modulo == 0:
        if n > 20:
            print (text_not)
        else:
            if n >= 6:
                print (text)
            else:
                if n >= 2:
                    print (text_not)
                    

