# 게임 개발

n,m=map(int,input().split())
x,y,d=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

dire={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]} #북동남서

cnt=1
matrix[x][y]=2
while True:
  for i in range(4):
    d=(4+d-1)%4 #왼쪽으로 방향 회전
    tmp_x=x+dire[d][0]
    tmp_y=y+dire[d][1]
    if tmp_x>-1 and tmp_x<m and tmp_y>-1 and tmp_y<n and matrix[tmp_x][tmp_y]==0:
      matrix[tmp_x][tmp_y]=2
      x,y=tmp_x,tmp_y
      cnt+=1
      break
  else:
    tmp_d=(4+d-2)%4 #뒤쪽 방향
    tmp_x=x+dire[d][0]
    tmp_y=y+dire[d][1]
    if not (tmp_x>-1 and tmp_x<m and tmp_y>-1 and tmp_y<n and matrix[tmp_x][tmp_y] in (0,2)):
      break
    x,y=tmp_x,tmp_y

print(matrix)
print(cnt)