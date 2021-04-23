# 수 정렬하기 2

# import sys
# import heapq

# n=int(sys.stdin.readline())
# numbers=[]
# for _ in range(n):
#   heapq.heappush(numbers,int(input()))
# print(numbers)
# for _ in range(n):
#   sys.stdout.write(str(heapq.heappop(numbers))+'\n')

import sys
n = int(input())
l = []
for i in range(n):
  l.append(int(sys.stdin.readline()))
for i in sorted(l):
  sys.stdout.write(str(i)+'\n')