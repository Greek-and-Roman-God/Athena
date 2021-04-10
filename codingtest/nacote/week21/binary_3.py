# 떡볶이 떡 만들기

n, m=map(int, input().split())
leng=list(map(int, input().split()))

start=0
end=max(leng)
center=(start+end)//2

ans=0
while start<=end:
  hap=0
  for l in leng:
    hap+=max(0,l-center)
  if hap>=m:
    ans=center
    start=center+1
  else:
    end=center-1
  center=(start+end)//2

print(ans)