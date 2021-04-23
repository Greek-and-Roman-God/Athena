# 전보
import heapq

INF=int(1e9)

n,m,c=map(int, input().split())
graph=[ [] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z))

dist=[INF]*(n+1)
queue=[]
heapq.heappush(queue,(0,c))
dist[c]=0
while queue:
    d, now=heapq.heappop(queue)
    if dist[now]<d:
        continue
    for i in graph[now]:
        cost=d+i[1]
        if cost<dist[i[0]]:
            dist[i[0]]=cost
            heapq.heappush(queue, (cost,i[0]))

count=0
min_dist=0
for d in dist:
    if d!=INF:
        count+=1
        min_dist=max(min_dist, d)

print(count-1, min_dist)