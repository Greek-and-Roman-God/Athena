# 영역 구하기
# https://www.acmicpc.net/problem/2583

# m,n,k=5, 7, 3
# coord=[[0, 2, 4, 4],
# [1, 1, 2, 5],
# [4, 0, 6, 2]]

m,n,k=map(int, input().split())
coord=[list(map(int, input().split())) for _ in range(k)]

matrix=[[0]*m for _ in range(n)]
for x1, y1, x2, y2 in coord:
  for i in range(x1,x2):
    for j in range(y1,y2):
      matrix[i][j]=1

dx=[0,0,1,-1] # 우좌상하
dy=[1,-1,0,0]

cnt=0
area=[]
while True:
  queue=[]
  flag=False
  for i in range(n):
    for j in range(m):
      if matrix[i][j]==0:
        queue.append([i,j])
        flag=True
        break
    if flag: break

  if len(queue)==0:
    break

  temp=1
  while queue:
    head=queue.pop(0)
    matrix[head[0]][head[1]]=2
    for i in range(4):
      x=head[0]+dx[i]
      y=head[1]+dy[i]
      if x>-1 and x<n and y>-1 and y<m and matrix[x][y]==0:
        queue.append([x,y])
        matrix[x][y]=2
        temp+=1
  area.append(temp)
  cnt+=1
area.sort()
print(cnt)
print(*area)
  