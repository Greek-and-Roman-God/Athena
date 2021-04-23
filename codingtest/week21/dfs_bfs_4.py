# 미로 탈출

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n,m=map(int, input().split())
matrix=[list(str(input())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

queue=deque()
queue.append([0,0])
matrix[0][0]=1
while queue:
  head=queue.popleft()
  for i in range(4):
    x=head[0]+dx[i]
    y=head[1]+dy[i]
    if x>-1 and x<n and y>-1 and y<m and matrix[x][y]=="1":
      queue.append([x,y])
      matrix[x][y]=matrix[head[0]][head[1]]+1

print(matrix[n-1][m-1])