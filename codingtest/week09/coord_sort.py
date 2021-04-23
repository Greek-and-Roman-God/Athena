# 좌표 정렬하기

# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

import sys

n=int(sys.stdin.readline())
coord=[]
for _ in range(n):
  coord.append(list(map(int,sys.stdin.readline().split())))

coord=sorted(coord, key=lambda x: (x[0], x[1]) )

for x,y in coord:
  print(f'{x} {y}')