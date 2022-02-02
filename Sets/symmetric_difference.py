#####################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true #
# By        -> jhosmanfrias, Feb-2022                                                                #
#####################################################################################################
M = int(input())

lM = set(map(int, input().split()))

N = int(input())

lN = set(map(int, input().split()))

uni = lM.difference(lN).union(lN.difference(lM))

l =list(uni)

l.sort()

for x in l:
    print(x)



