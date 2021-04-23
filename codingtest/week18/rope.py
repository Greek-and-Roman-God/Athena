# 로프
# https://www.acmicpc.net/problem/2217

# 2
# 10
# 15

n=int(input())
rope=[0]*n
for i in range(n):
  rope[i]=int(input())
rope.sort()

max_weight=0
for i in range(n):
  max_weight=max(rope[i]*(n-i), max_weight)

print(max_weight)