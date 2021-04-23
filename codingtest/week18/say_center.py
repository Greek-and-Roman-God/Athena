# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5

import heapq
import sys

n=int(sys.stdin.readline())
max_heap=[]
min_heap=[]

temp=int(sys.stdin.readline())
heapq.heappush(max_heap, [-temp, temp])
print(max_heap[0][1])

for i in range(1,n):
  temp=int(sys.stdin.readline())
  if max_heap[0][1]<temp:
    heapq.heappush(min_heap, temp)
  else:
    heapq.heappush(max_heap, [-temp,temp])
  if len(min_heap)<len(max_heap):
    heapq.heappush(min_heap, heapq.heappop(max_heap)[1])
  if len(min_heap)>len(max_heap):
    pop_temp=heapq.heappop(min_heap)
    heapq.heappush(max_heap, [-pop_temp,pop_temp])
  # print(max_heap)
  # print(min_heap)
  print(max_heap[0][1])