# 최단 경로
# https://www.acmicpc.net/problem/1753

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9) # 10억

def dijkstra(dist,start):
    q=[]
    heapq.heappush(q, (0,start))
    dist[start]=0
    while q:
        d,now=heapq.heappop(q)
        if dist[now]<d:
            continue
        for i in graph[now]:
            cost=d+i[1]
            if dist[i[0]]>cost:
                dist[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))


v, e=map(int, input().split())
k=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

dist=[INF]*(v+1)
dijkstra(dist, k)

for d in dist[1:]:
    if d>=INF:
        print("INF")
    else:
        print(d)