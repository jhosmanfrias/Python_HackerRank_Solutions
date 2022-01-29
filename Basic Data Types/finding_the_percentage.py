#######################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                                 #
#######################################################################################################

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
for x in student_marks:
    if query_name == x:
        print("{:.2f}".format(((student_marks[x][0]+student_marks[x][1]+student_marks[x][2])/3)))

