#################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                           #
#################################################################################################

def print_rangoli(size):
    rag = "abcdefghijklmnopqrstuvwxyz"
    mid = size * 2 - 1
    top = size + (size - 1) * 3
    for x in range(mid):
        if x <= int(mid/2):
            aa = rag[int(mid/2)-x]
            for y in range(int(mid/2)-x,int(mid/2)):
                aa = rag[y+1] + "-" + aa + "-" + rag[y+1]
            print (aa.center(top, "-"))
        if x > int(mid/2):
            aa = rag[x-int(mid/2)]
            for y in range(x-int(mid/2),int(mid/2)):
                aa = rag[y+1] + "-" + aa + "-" + rag[y+1]
            print (aa.center(top, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
