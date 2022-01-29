####################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                              #
####################################################################################################


from collections import Counter
n = int(input())

shoes = Counter(input().split())

m = int(input())

total = 0

for x in range(m):
    a, b = input().split()
    if a in shoes and shoes[a] > 0:
        shoes[a] -= 1
        total += int(b)

print (total)
