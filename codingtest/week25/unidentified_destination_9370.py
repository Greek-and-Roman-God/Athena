# 미확인 도착지
# https://www.acmicpc.net/problem/9370

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

def dijkstra(distance, start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

T=int(input())
for _ in range(T):
    n,m,t=map(int, input().split())
    s,g,h=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    gh=0
    for _ in range(m):
        a,b,d=map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        if a in (g,h) and b in (g,h):
            gh=d
    x=[]
    for _ in range(t):
        x.append(int(input()))
    x.sort()
    
    distance=[INF]*(n+1)
    distance1=[INF]*(n+1)
    distance2=[INF]*(n+1)

    dijkstra(distance, s)
    dijkstra(distance1, g)
    dijkstra(distance2, h)

    answer=[INF]*(n+1)
    for i in x:
        answer[i]=min(distance2[s]+distance1[i]+gh, distance1[s]+distance2[i]+gh)

    for i in x:
        if answer[i]<=INF and answer[i]<=distance[i]:
            print(i, end=' ')
    print()