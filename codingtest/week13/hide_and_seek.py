# 숨바꼭질
from collections import deque

n, k = map(int, input().split())

visit = [False for i in range(100001)]
queue=deque()
queue.append([n, 0])
while queue:
  p, d = queue[0][0], queue[0][1]
  if p == k:
    break
  queue.popleft()
  visit[p]=True
  if p - 1 >= 0 and not visit[p - 1]:
    queue.append([p - 1, d + 1])
  if p + 1 <= 100000 and not visit[p + 1]:
    queue.append([p + 1, d + 1])
  if p * 2 <= 100000 and not visit[p * 2]:
    queue.append([p * 2, d + 1])
print(queue[0][1])