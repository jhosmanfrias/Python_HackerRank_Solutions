
##################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                            #
##################################################################################################

n, m = input().split()

n = int(n)
m = int(m)
pu = ".|."

for x in range(n):
    if x == int(n/2):
        print ("WELCOME".center(int(m), "-"), end = "")
    else:
        if x < int(n/2):
            print ((pu*(2*x+1)).center(int(m), "-"), end = "")
        else:
            if x > int(n/2):
                xx = n - x - 1
                print ((pu*(2*xx+1)).center(int(m), "-"), end = "")
    print()

