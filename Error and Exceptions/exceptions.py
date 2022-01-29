###########################################################################################
# Challenge -> https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                     #
###########################################################################################

n = int(input())

for x in range (n):
    a, b = input().split()
    try:
        print (int(int(a) / int(b)))
    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print ("Error Code: " + str(e))



