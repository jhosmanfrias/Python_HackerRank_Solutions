##############################################################################################
# Challenge -> https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                        #
##############################################################################################

def count_substring(string, sub_string):
    i = 0
    for x in range (len(string)):
        if string[x:].startswith(sub_string):
            i += 1
    return i

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
