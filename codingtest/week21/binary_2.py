# 부품 찾기

n=int(input())
ns=list(map(int,input().split()))

m=int(input())
ms=list(map(int,input().split()))

ns.sort()
for i in ms:
  ans="no"
  start=0
  end=n-1
  center=(end+start)//2
  while start<=end:
    if ns[center]==i:
      ans="yes"
      break
    if ns[center]<i:
      start=center+1
    else:
      end=center-1
    center=(start+end)//2
  print(ans)
