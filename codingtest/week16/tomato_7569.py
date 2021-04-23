# 토마토

# 5 3 1
# 0 -1 0 0 0
# -1 -1 0 1 1
# 0 0 0 1 1

# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0

# 4 3 2
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# -1 -1 -1 -1
# 1 1 1 -1

from collections import deque

m, n, h=map(int, input().split())
tomato=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx=[0,0,1,-1] #위 아래 오른쪽 왼쪽
dy=[1,-1,0,0]

queue=deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k]==1:
        queue.append([i,j,k])

while queue:
  head=queue.popleft()
  for i in range(4):
    x=head[1]+dx[i]
    y=head[2]+dy[i]
    if x>-1 and x<n and y>-1 and y<m and tomato[head[0]][x][y]==0:
      queue.append([head[0],x,y])
      tomato[head[0]][x][y]=tomato[head[0]][head[1]][head[2]]+1
  for i in (-1,1):
    z=head[0]+i
    if z>-1 and z<h and tomato[z][head[1]][head[2]]==0:
      queue.append([z,head[1],head[2]])
      tomato[z][head[1]][head[2]]=tomato[head[0]][head[1]][head[2]]+1
    
ans=0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k]==0:
        print(-1)
        exit()
      if ans<tomato[i][j][k]:
        ans=tomato[i][j][k]
print(ans-1)