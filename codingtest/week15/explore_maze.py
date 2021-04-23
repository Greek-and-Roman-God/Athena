# 미로 탐색

# 4 6
# 101111
# 101010
# 101011
# 111011

# 4 6
# 120890
# 230780
# 345678
# 456709

n, m=map(int, input().split())
maze=[list(map(int,list(input()))) for _ in range(n)]

dx=[0,0,1,-1] #위 아래 오른쪽 왼쪽
dy=[1,-1,0,0]

queue=[[0,0]]
while queue:
  head=queue.pop(0)
  for i in range(4):
    x=head[0]+dx[i]
    y=head[1]+dy[i]
    if x>-1 and x<n and y>-1 and y<m and maze[x][y]==1:
      queue.append([x,y])
      maze[x][y]=maze[head[0]][head[1]]+1
print(maze[n-1][m-1])