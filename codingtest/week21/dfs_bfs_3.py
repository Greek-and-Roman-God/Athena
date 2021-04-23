# 음료수 얼려 먹기

# 00110
# 00011
# 11111
# 00000
from collections import deque

n,m=map(int,input().split())
ice=[list(map(int, str(input()))) for i in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

cnt=0
for i in range(n):
  for j in range(m):
    if ice[i][j]==1: continue
    cnt+=1
    queue=deque()
    queue.append([i,j])
    ice[i][j]=1
    while queue:
      head=queue.popleft()
      for k in range(4):
        x=head[0]+dx[k]
        y=head[1]+dy[k]
        if x>-1 and x<n and y>-1 and y<m and ice[x][y]==0:
          queue.append([x,y])
          ice[x][y]=1

print(cnt)