########################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true #
# By        -> jhosmanfrias, Feb-2022                                                                  #
########################################################################################################
n = input()
nums = input().split()
print (all(int(i) > 0 for i in nums) and any(x == x[::-1] for x in nums))
