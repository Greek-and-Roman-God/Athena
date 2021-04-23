# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 3
# 10
# 20
# 40
import heapq

n=int(input())
cards=[]
for _ in range(n):
  heapq.heappush(cards, int(input()))
total=0
while len(cards)>1:
  a=heapq.heappop(cards)
  b=heapq.heappop(cards)
  heapq.heappush(cards, a+b)
  total+=a+b
print(total)

