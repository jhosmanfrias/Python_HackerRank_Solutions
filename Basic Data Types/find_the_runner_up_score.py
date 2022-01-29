#####################################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                                               #
#####################################################################################################################

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
runup = list(dict.fromkeys(arr))

print (runup[len(runup)-2])

