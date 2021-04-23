# 정수 삼각형

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

n=int(input())
tri=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  if i==0: continue
  for j in range(len(tri[i])):
    temp=0
    if j==0:
      temp=tri[i-1][0]
    elif j==len(tri[i])-1:
      temp=tri[j-1][-1]
    else:
      temp=max(tri[i-1][j-1],tri[i-1][j])
    tri[i][j]+=temp
print(max(tri[-1]))