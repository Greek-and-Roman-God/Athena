# 운동
# https://www.acmicpc.net/problem/1956

# 3 4
# 1 2 1
# 3 2 1
# 1 3 5
# 2 3 2

import sys
input=sys.stdin.readline
INF=int(1e9)

v,e=map(int, input().split())
s = [[INF] * (v+1) for i in range(v+1)]
for i in range(e):
    a,b,c=map(int, input().split())
    s[a][b]=c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            if s[i][j]>s[i][k]+s[k][j]:
                s[i][j]=s[i][k]+s[k][j]

result=INF
for i in range(1, v+1):
    result=min(result,s[i][i])
if result==INF:
    print(-1)
else:
    print(result)