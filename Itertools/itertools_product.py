##################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-202                                                             #
##################################################################################################

list1 = []
list2 = []

list1 = input().split()
list2 = input().split()

list1a = [int(x) for x in list1]
list1b = [int(x) for x in list2]

from itertools import product

for x in list(product(list1a, list1b)):
    print(x, end = " ") 

