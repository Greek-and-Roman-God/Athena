# 연료 채우기
# https://www.acmicpc.net/problem/1826

# 4
# 4 4
# 5 2
# 11 5
# 15 10
# 25 10

import sys
import heapq

n=int(sys.stdin.readline())
gas=[]
for _ in range(n):
  heapq.heappush(gas,list(map(int, sys.stdin.readline().split())))
l,p=map(int, sys.stdin.readline().split())

capable=[]
cnt=0
while p<l:
  while gas and gas[0][0]<=p:
    heapq.heappush(capable, -heapq.heappop(gas)[1])
  if not capable:
    cnt=-1
    break
  p+=-heapq.heappop(capable)
  cnt+=1

print(cnt)