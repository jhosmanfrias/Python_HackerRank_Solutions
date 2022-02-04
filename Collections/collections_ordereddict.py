###########################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true #
# By        -> jhosmanfrias, Feb-2022                                                                     #
###########################################################################################################
from collections import OrderedDict

n = int(input())

items = OrderedDict()

for x in range(n):
    item = input()
    sp = item.rfind(" ", 0, len(item))
    name = item[0:sp]
    price = int(item[sp:len(item)].strip())
    if name in items:
        items[name] += price
    else:
        items[name] = price
    #print(item + " - name: " + name + "; price: " + price)
    
for x in items:
    print(x + " " + str(items[x]))
