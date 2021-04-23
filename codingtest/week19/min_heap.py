# 최소 힙
# https://www.acmicpc.net/problem/1927

# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
import sys
import heapq

n=int(sys.stdin.readline())
min_heap=[]
for _ in range(n):
  comm=int(sys.stdin.readline())
  if comm==0:
    if min_heap:
      print(heapq.heappop(min_heap))
    else:
      print(0)
    continue
  heapq.heappush(min_heap, comm)
