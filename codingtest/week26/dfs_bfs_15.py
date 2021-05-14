# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque

n,m,k,x=map(int, input().split())
data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    data[a].append(b)

queue=deque()
queue.append(x)
answer=[-1]*(n+1)
answer[x]=0
while queue:
    now=queue.popleft()
    for i in data[now]:
        if answer[i]==-1:
            answer[i]=answer[now]+1
            queue.append(i)
flag=True
for i in range(1, n+1):
    if answer[i]==k:
        print(i)
        flag=False
if flag: print(-1)