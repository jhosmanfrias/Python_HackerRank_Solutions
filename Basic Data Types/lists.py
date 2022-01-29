#############################################################################################
# Challenge -> https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                       #
#############################################################################################

if __name__ == '__main__':
    N = int(input())
    
    arr = list()
    
    for _ in range(N):
        line = input()
        if line.startswith ("insert"):
            arr.insert(int(line.split(" ")[1]), int(line.split(" ")[2]))
        if line.startswith ("print"):
            print(arr)
        if line.startswith ("remove"):
            arr.remove(int(line.split(" ")[1]))
        if line.startswith ("append"):
            arr.append(int(line.split(" ")[1]))
        if line.startswith ("pop"):
            arr.pop()
        if line.startswith ("reverse"):
            arr.reverse()
        if line.startswith ("sort"):
            arr.sort()

