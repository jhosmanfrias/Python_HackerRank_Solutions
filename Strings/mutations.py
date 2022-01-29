################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-202                                                           #
################################################################################################

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
