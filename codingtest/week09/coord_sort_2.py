# 좌표 정렬하기 2

import sys

n=int(sys.stdin.readline())
coord=[]
for _ in range(n):
  coord.append(list(map(int,sys.stdin.readline().split())))

coord=sorted(coord, key=lambda x: (x[1], x[0]) )

for x,y in coord:
  print(f'{x} {y}')