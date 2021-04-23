# 절댓값 힙
# https://www.acmicpc.net/problem/11286

# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0

import sys
import heapq

n=int(sys.stdin.readline())
abs_heap=[]

for _ in range(n):
  comm=int(sys.stdin.readline())
  if comm==0:
    if abs_heap:
      temp=heapq.heappop(abs_heap)
      # if abs_heap and temp[0]==abs_heap[0][0] and temp[1]>abs_heap[0][1]:
      #   temp[1]*=-1
      #   abs_heap[0][1]*=-1
      print(temp[1])
    else:
      print(0)
    continue
  heapq.heappush(abs_heap, [abs(comm), comm])