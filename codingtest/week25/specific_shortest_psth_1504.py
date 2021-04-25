# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

def dijkstra(dist, start):
    q=[]
    heapq.heappush(q, (0,start))
    dist[start]=0
    while q:
        d, now=heapq.heappop(q)
        if dist[now]<d:
            continue
        for i in graph[now]:
            cost=d+i[1]
            if dist[i[0]]>cost:
                dist[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))

n, e=map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int, input().split())

dist=[INF]*(n+1)
dist1=[INF]*(n+1)
dist2=[INF]*(n+1)

dijkstra(dist,1)
dijkstra(dist1,v1)
dijkstra(dist2,v2)

answer=min(dist[v1]+dist1[v2]+dist2[n], dist[v2]+dist2[v1]+dist1[n])
print(answer if answer<INF else -1)