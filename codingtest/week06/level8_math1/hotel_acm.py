# ACM 호텔

t=int(input())

for _ in range(t):
  h, w, n=map(int,input().split())
  y=n%h
  x=n//h+1
  if n%h == 0:
    y=h
    x-=1
  if x<10:
    y=y*10
  print(str(y)+str(x))