# 포도주 시식
# https://www.acmicpc.net/problem/2156

# 6
# 6
# 10
# 13
# 9
# 8
# 1

# 6
# 1000 1000 1    1    1000 1000
# 1000 2000 1001 2001 

n=int(input())
wine=[0]*10000
for i in range(n):
  wine[i]=int(input())

dp=[0]*10000
dp[0]=wine[0]
dp[1]=wine[0]+wine[1]
dp[2]=max(wine[0]+wine[2],wine[1]+wine[2])
dp[3]=max(dp[1]+wine[3], dp[0]+wine[2]+wine[3])
for i in range(4, n):
  dp[i]=max(dp[i-2]+wine[i] , dp[i-3]+wine[i-1]+wine[i], dp[i-4]+wine[i-1]+wine[i])

print(max(dp))