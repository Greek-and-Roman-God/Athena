# KCM Travel
# https://www.acmicpc.net/problem/10217

# 2
# 3 100 3
# 1 2 1 1
# 2 3 1 1
# 1 3 3 30
# 4 10 4
# 1 2 5 3
# 2 3 5 4
# 3 4 1 5
# 1 3 10 6

import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n,m,k=map(int, input().split())
    graph=[]
    for _ in range(k):
        u,v,c,d=map(int, input().split())
        