##################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-202                                                             #
##################################################################################################

if __name__ == '__main__':
    s = input()
    
    bo = False
    for x in range(len(s)):
        if s[x].isalnum():
            bo = True
            break
    print (bo)
    
    bo = False
    for x in range(len(s)):
        if s[x].isalpha():
            bo = True
            break
    print (bo)

    bo = False
    for x in range(len(s)):
        if s[x].isdigit():
            bo = True
            break
    print (bo)

    bo = False
    for x in range(len(s)):
        if s[x].islower():
            bo = True
            break
    print (bo) 

    bo = False
    for x in range(len(s)):
        if s[x].isupper():
            bo = True
            break
    print (bo)    
    
    

