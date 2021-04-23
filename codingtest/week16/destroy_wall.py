# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

from collections import deque

# n,m=6, 4
# maze=[[0,1,0,0],
# [1,1,1,0],
# [1,0,0,0],
# [0,0,0,0],
# [0,1,1,1],
# [0,0,0,0]]

n, m=map(int, input().split())
maze=[list(map(int,list(input()))) for _ in range(n)]

def bfs():
  dx=[0,0,1,-1] #위 아래 오른쪽 왼쪽
  dy=[1,-1,0,0]
  check=[[[0,0] for _ in range(m)] for _ in range(n)]
  check[0][0][1]=1
  queue=deque()
  queue.append([0,0,1])
  while queue:
    a, b, w=queue.popleft()
    if a==n-1 and b==m-1:
      return check[a][b][w]
    for i in range(4):
      x=a+dx[i]
      y=b+dy[i]
      if x>-1 and x<n and y>-1 and y<m:
        if maze[x][y]==1 and w==1:
          check[x][y][0]=check[a][b][1]+1
          queue.append([x,y,0])
        if maze[x][y]==0 and check[x][y][w]==0:
          check[x][y][w]=check[a][b][w]+1
          queue.append([x,y,w])
  return -1

print(bfs())

