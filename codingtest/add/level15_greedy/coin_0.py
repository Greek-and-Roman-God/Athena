# 동전 0

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000


n, k=map(int, input().split())
coin=[]
for _ in range(n):
  coin.insert(0,int(input())) #내림차순으로 정렬

idx=cnt=0
while k>0:
  if k>=coin[idx]:
    cnt+=k//coin[idx]
    k=k%coin[idx]
  idx+=1
print(cnt)