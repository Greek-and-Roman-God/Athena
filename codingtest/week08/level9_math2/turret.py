# 터렛
# 왜 맞았는지 모르겠음

t=int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2= map(int, input().split())
  dist=( (x1-x2)**2 + (y1-y2)**2 )**0.5
  r_dist=abs(r1-r2)
  if dist==0:
    if r1==r2:
      cnt=-1
    else:
      cnt=0
  else:
    if dist<r1+r2 and r_dist<dist:
      cnt=2
    elif dist==r1+r2 or r_dist==dist:
      cnt=1
    else:
      cnt=0
  print(cnt)