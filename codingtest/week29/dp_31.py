# 금광

t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    temp=list(map(int, input().split()))
    
    gold=[]
    for i in range(n):
        gold.append(temp[i*m:(i*m)+m])
    
    for i in range(1,m):
        for j in range(n):
            if j==0:
                gold[j][i]+=max(gold[j][i-1],gold[j+1][i-1])
            elif j==(n-1):
                gold[j][i]+=max(gold[j][i-1],gold[j-1][i-1])
            else:
                gold[j][i]+=max(gold[j][i-1],gold[j-1][i-1],gold[j+1][i-1])
    
    ans=0
    for i in range(n):
        ans=max(ans,gold[i][m-1])
    print(ans)