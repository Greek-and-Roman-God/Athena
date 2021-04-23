# 하노이 탑 이동 순서

def hanoi(n, x, y, archive):
  if n>1:
    hanoi(n-1,x,6-x-y,archive)
  archive.append([x,y])
  if n>1:
    hanoi(n-1,6-x-y,y,archive)

n=int(input())
archive=[]
hanoi(n, 1, 3, archive)
print(len(archive))
for i in archive:
  print(f'{i[0]} {i[1]}')