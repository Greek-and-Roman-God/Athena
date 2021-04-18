# 미래도시

INF=int(1e9)

n,m=map(int, input().split())
matrix=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    matrix[i][i]=0
for _ in range(m):
    a,b=map(int, input().split())
    matrix[a][b]=1
    matrix[b][a]=1
x,k=map(int, input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i][j]=min(matrix[i][j], matrix[i][k]+matrix[k][j])

answer=matrix[1][k]+matrix[k][x]
answer=-1 if answer>=INF else answer

print(answer)