#####################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                               #
#####################################################################################################

from collections import defaultdict


n_a, n_b = input().split()

group_a = defaultdict(list)

for x in range(int(n_a)):
    entrada = str(input().strip())
    group_a[entrada].append(x+1)
    

for y in range(int(n_b)):
    entrada = str(input().strip())
    if entrada in group_a: 
        print (*group_a[entrada])
    else:
        print (-1)
    

