# OX퀴즈
# https://www.acmicpc.net/problem/8958

t=int(input())
for _ in range(t):
    score=list(input())
    ans=0
    tmp_score=0
    for s in score:
        if s=="O":
            tmp_score+=1
        if s=="X":
            tmp_score=0
        ans+=tmp_score
    print(ans)