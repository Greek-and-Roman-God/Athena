# 최대 힙
# https://www.acmicpc.net/problem/11279

# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0
import sys
import heapq

n=int(sys.stdin.readline())
max_heap=[]
for _ in range(n):
  comm=int(sys.stdin.readline())
  if comm==0:
    if max_heap:
      print(-heapq.heappop(max_heap))
    else:
      print(0)
    continue
  heapq.heappush(max_heap, -comm)