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


# https://developmentdiary.tistory.com/401
import sys
 
T=int(input())
INF=sys.maxsize
 
for _ in range(T):
    N,M,K=map(int,sys.stdin.readline().split())#공항수,지원비용,티켓정보수
    ticket=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,sys.stdin.readline().split())#출발,도착,비용,소요시간
        ticket[u].append([v,c,d])
 
 
    DP=[[INF for _ in range(M+1)] for _ in range(N+1)]#열:비용 행:n까지갈때
    DP[1][0]=0#1->1로 갔을때 비용은0 시간도 0
    # [1]은 1번 공항, [0]은 0원으로, =0은 0시간이 걸리다는 뜻
    # DP[2][3]=7 이라면 2번공항으로 3원을 소요하여 7시간만에 도착한다는 의미
    for c in range(M+1):
        for d in range(1,N+1):
            if DP[d][c]==INF:continue#c의 비용으로 d에 도착하는 경우가 없다면
            t=DP[d][c]#c의 비용으로 d에 도착햇을때의 소요시간
            for dv,dc,dd in ticket[d]:#d에서 출발하는 모든경우
                if dc+c>M:#비용이 초과될경우 넘어간다
                    continue
                DP[dv][dc+c]=min(DP[dv][dc+c],t+dd)#이전에 저장된값과 비교하여 작다면 갱신해준다
 
    result=min(DP[N])#N에 도착할때 최소소요시간
 
    if result==INF:
        print('Poor KCM')
    else:
        print(result)
