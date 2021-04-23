# 단지번호 붙이기

def bfs(n, head, matrix):
  dx=[0,0,1,-1] #위 아래 오른쪽 왼쪽
  dy=[1,-1,0,0]
  cnt=0
  queue=[head]
  while queue:
    cnt+=1
    head=queue.pop(0)
    matrix[head[0]][head[1]]=0
    for i in range(4):
      x=head[0]+dx[i]
      y=head[1]+dy[i]
      if x>-1 and x<n and y>-1 and y<n and matrix[x][y]==1:
        queue.append([x,y])
        matrix[x][y]=0
  return cnt

n=7
matrix=[
[0,1,1,0,1,0,0],
[0,1,1,0,1,0,1],
[1,1,1,0,1,0,1],
[0,0,0,0,1,1,1],
[0,1,0,0,0,0,0],
[0,1,1,1,1,1,0],
[0,1,1,1,0,0,0]]

# n=int(input())
# matrix=[]
# for _ in range(n):
#   matrix.append(list(map(int,list(input()))))

ans=[]
for i in range(n):
  for j in range(n):
    if matrix[i][j]==1:
      ans.append(bfs(n, [i,j], matrix))
print(len(ans))
ans.sort()
for a in ans:
  print(a)