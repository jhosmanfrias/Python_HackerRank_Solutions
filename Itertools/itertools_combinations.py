#######################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true #
# By        -> jhosmanfrias, Feb-2022                                                                 #
#######################################################################################################
from itertools import combinations

word, n = input().split()

l2 = []

def order (t2):
    t3 = []
    t3[:0] = t2
    t3.sort()
    return "".join(map(str,t3))

for x in range(1, int(n)+1):
    l = []
    l = list(combinations(word, x))
    l.sort()
    for y in range(len(l)):
        p = l[y]
        t = ""
        for z in range(0, len(p)):
            t = t + p[z] 
            if z == len(p)-1:
                l2.append(order(t))
    
l3 = []

for z in range(1, int(n)+1):
    for w in range(len(l2)):

        if len(l2[w]) == z:
            l3.append(l2[w])
   
    l3.sort()
    print(*l3, sep = "\n")
    l3.clear()


