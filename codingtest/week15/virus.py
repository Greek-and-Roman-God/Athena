# 바이러스

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

n=int(input())
m=int(input())
network=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b=map(int, input().split())
  network[a][b]=1
  network[b][a]=1

check=[False]*(n+1)
check[1]=True
cnt=0
queue=[1]
while queue:
  head=queue.pop(0)
  for i in range(1, n+1):
    if not check[i] and network[head][i]==1:
      queue.append(i)
      check[i]=True
      cnt+=1
print(cnt)
