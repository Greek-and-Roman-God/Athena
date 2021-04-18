# 효율적인 화폐 구성

n,m=map(int, input().split()) # 3 7
coins=[int(input()) for _ in range(n)] # 2 3 5

dp=[10001]*(m+1)

dp[0]=0
for i in range(n):
  for j in range(coins[i], m+1):
    if dp[j-coins[i]]!=1001:
      dp[j]=min(dp[j], dp[j-coins[i]]+1)

if dp[m]==10001:
  print(-1)
else:
  print(dp[m])