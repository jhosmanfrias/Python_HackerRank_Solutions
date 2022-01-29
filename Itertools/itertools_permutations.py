#######################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                                 #
#######################################################################################################


from itertools import permutations

a = ""
b = 0

a, b = input().split()

l = list(permutations(a, int(b)))

l2 = []

for x in l:
    loc = ""
    for y in x:
        loc += y
    l2.append(loc)

l2.sort()

for x in l2:
    print(x)

