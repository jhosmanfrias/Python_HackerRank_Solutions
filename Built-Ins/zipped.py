#######################################################################################
# Challenge -> https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                 #
#######################################################################################

import sys

i = 0
arr2 = []

x, n = input().split(" ")


for i in range (int(n)):
    arr2.append(input())

for s in range(int(x)):
    sum = 0
    for u in range(int(n)):
        loc = arr2[u].split(" ")
        sum = sum + float(loc[s].strip()) 
    print (sum/int(n))
    
