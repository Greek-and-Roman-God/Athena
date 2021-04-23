# 7576번 토마토

# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

from collections import deque

m, n=map(int, input().split())
tomato=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,1,-1] #위 아래 오른쪽 왼쪽
dy=[1,-1,0,0]

queue=deque()
for i in range(n):
  for j in range(m):
    if tomato[i][j]==1:
      queue.append([i,j])

while queue:
  head=queue.popleft()
  for i in range(4):
    x=head[0]+dx[i]
    y=head[1]+dy[i]
    if x>-1 and x<n and y>-1 and y<m and tomato[x][y]==0:
      queue.append([x,y])
      tomato[x][y]=tomato[head[0]][head[1]]+1

ans=0
for i in range(n):
  for j in range(m):
    if tomato[i][j]==0:
      print(-1)
      exit()
    if ans<tomato[i][j]:
      ans=tomato[i][j]
print(ans-1)