# 치즈
# https://www.acmicpc.net/problem/2636

# n,m=13,12
# che=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
# [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
# [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
# [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
# [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n,m=map(int, input().split())
che=[list(map(int, input().split())) for _ in range(n)]

dx=[0,0,1,-1] # 우좌상하
dy=[1,-1,0,0]

time_cnt=0
last_cnt=0
while True:
  queue=[[0,0]]
  temp=0
  remove=[]
  while queue:
    head=queue.pop(0)
    for i in range(4):
      x=head[0]+dx[i]
      y=head[1]+dy[i]
      if x>-1 and x<n and y>-1 and y<m:
        if che[x][y]==0:
          che[x][y]=-1
          queue.append([x,y])
        if che[x][y]==1:
          che[x][y]=-1
          temp+=1
  if temp==0:
    break
  for i in range(n):
    for j in range(m):
      if che[i][j]==-1:
        che[i][j]=0
  last_cnt=temp
  time_cnt+=1

print(time_cnt)
print(last_cnt)