#########################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                                   #
#########################################################################################################

def print_formatted(number):
    x = 1
    top = number 
    for x in range(1, top+1):
        l = len(bin(top))-2
        print("{x1:>{w2}d} {x2:>{w1}o} {x3:>{w1}X} {x4:>{w1}b}".format(x1=x, x2=x, x3=x, x4=x, w1=l, w2=l))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
