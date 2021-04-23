# 치킨 배달

from itertools import combinations
 
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]

# n, m=5, 3
# board=[[0, 0, 1, 0, 0],
# [0, 0, 2, 0, 1],
# [0, 1, 2, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 0, 2]]
 
n, m=5, 2
board=[[0, 2, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[2, 0, 0, 1, 1],
[2, 2, 0, 1, 2]]

house = []
chicken = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1: house.append((i, j))
    elif board[i][j] == 2: chicken.append((i, j))
 
minv = float('inf') #양의 무한대
for ch in combinations(chicken, m):
  #print(ch)
  sumv = 0
  for home in house:
    # sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
    dist=[]
    for i in ch:
      dist.append(abs(home[0]-i[0])+abs(home[1]-i[1]))
    sumv+=min(dist)
    if minv <= sumv: break # sumv가 minv보다 커지는순간 더 더할 필요가 없으므로 break
  if sumv < minv: minv = sumv
 
print(minv)