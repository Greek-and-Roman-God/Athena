# 경쟁적 전염
from collections import deque

n,k=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
s,x,y=map(int, input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
for _ in range(s):
    for now in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==now:
                    queue.append([i,j])
    while queue:
        i,j=queue.popleft()
        for d in range(4):
            tmpx,tmpy=i+dx[d],j+dy[d]
            if tmpx>-1 and tmpx<n and tmpy>-1 and tmpy<n and graph[tmpx][tmpy]==0:
                graph[tmpx][tmpy]=graph[i][j]

print(graph[x-1][y-1])