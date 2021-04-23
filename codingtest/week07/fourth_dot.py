# 네 번째 점

coord=[]
for _ in range(3):
  coord.append(list(map(int,input().split())))

if coord[0][0] not in (coord[1][0],coord[2][0]):
  x=coord[0][0]
elif coord[1][0] not in (coord[0][0],coord[2][0]):
  x=coord[1][0]
else:
  x=coord[2][0]

if coord[0][1] not in (coord[1][1],coord[2][1]):
  y=coord[0][1]
elif coord[1][1] not in (coord[0][1],coord[2][1]):
  y=coord[1][1]
else:
  y=coord[2][1]

print(f'{x} {y}')