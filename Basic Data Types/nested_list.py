############################################################################################
# Challenge -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                      #
############################################################################################

if __name__ == '__main__':
    stu = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name,score])
        scores.append(score)
        
scores.sort()

scores = list(dict.fromkeys(scores))

sc = scores[1]
st = []

for x in range(len(stu)):
    if stu[x][1] == sc:
        st.append(stu[x][0])
        
st.sort()

for x in range(len(st)):
    print (st[x])

