##########################################################################################
# Challenge -> https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                    #
##########################################################################################

def swap_case(s):
    temp = ""
    for x in s:
        if x.isupper():
            temp += x.lower()
        else:
            temp += x.upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
