# 프린터 큐
# https://www.acmicpc.net/problem/1966

# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1
from collections import deque

t=int(input())
for _ in range(t):
  n, m=map(int, input().split())
  queue=deque((map(int, input().split())))
  cnt=0

  while True:
    target=queue.popleft()
    for q in queue:
      if q>target:
        queue.append(target)
        break
    else:
      cnt+=1
      if m==0:
        print(cnt)
        break
    m=(m-1+n-cnt)%(n-cnt)


  
