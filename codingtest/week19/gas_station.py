# 주유소
# https://www.acmicpc.net/problem/13305

# 4
# 2 3 1
# 5 2 4 1

# 4
# 3 3 4
# 1 1 1 1

import sys

n=int(sys.stdin.readline())
dist=list(map(int, sys.stdin.readline().split()))
price=list(map(int, sys.stdin.readline().split()))

total=price[0]*dist[0] 
min_price=price[0]
for i in range(1,n-1):
  min_price=min(min_price, price[i])
  total+=min_price*dist[i]

print(total)