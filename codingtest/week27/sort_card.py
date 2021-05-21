# 카드 정렬하기

import heapq

n=int(input())
card=[]
for _ in range(n):
    heapq.heappush(card, int(input()))

total=0
while len(card)>1:
    a=heapq.heappop(card)
    b=heapq.heappop(card)
    total+=a+b
    heapq.heappush(card, a+b)

print(total)