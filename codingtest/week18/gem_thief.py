# 보석 도둑
# https://www.acmicpc.net/problem/1202

# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2
import heapq
import sys

n, k=map(int, sys.stdin.readline().split())
gem=[]
for _ in range(n):
  weight, price=map(int, sys.stdin.readline().split())
  heapq.heappush(gem,[weight, price])
bags=[]
for i in range(k):
  heapq.heappush(bags,int(sys.stdin.readline()))

answer=0
capable_gem=[]
for _ in range(k):
  bag=heapq.heappop(bags)
  while gem and bag>=gem[0][0]:
    heapq.heappush(capable_gem, -heapq.heappop(gem)[1])
  if capable_gem:
    answer-= heapq.heappop(capable_gem)

print(answer)
