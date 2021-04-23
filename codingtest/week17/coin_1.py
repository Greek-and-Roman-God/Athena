# 동전 1
# https://www.acmicpc.net/problem/2293

# 3 10
# 1
# 2
# 5

n,k=map(int,input().split())
coins=[0]*n
for i in range(n):
  coins[i]=int(input())

dp=[0]*(k+1)
for i in range(k+1):
  if i%coins[0]==0:
    dp[i]=1

for i in range(1, n):
  for j in range(k+1):
    if j==coins[i]:
      dp[j]=dp[j]+1
    if j>coins[i]:
      dp[j]=dp[j]+dp[j-coins[i]]
print(dp[k])

