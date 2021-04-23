# 1이 될 때까지

n,k=map(int,input().split())

cnt=0
while n!=1:
  cnt+=n%k+1
  n=n//k

print(cnt)