# 보물
# https://www.acmicpc.net/problem/1026

# 5
# 1 1 1 6 0
# 2 7 8 3 1

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
rank=[-1]*n
a.sort()
for i in range(n):
  temp=n-1
  for j in range(n):
    if b[i]>b[j]:
      temp-=1
  while temp in rank:
    temp-=1
  rank[i]=temp

answer=0
for i in range(n):
  answer+=a[rank[i]]*b[i]

print(answer)