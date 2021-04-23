# 요세푸스 문제
# https://www.acmicpc.net/problem/1158

# 7 3

from collections import deque

n,k=map(int, input().split())
queue=deque()

for i in range(1,n+1):
  queue.append(i)

answer=[]
while queue:
  for i in range(k-1):
    queue.append(queue.popleft())
  answer.append(queue.popleft())

print("<", end="")
for ans in answer[:n-1]:
  print(ans, end=", ")
print(answer[n-1], end="")
print(">")