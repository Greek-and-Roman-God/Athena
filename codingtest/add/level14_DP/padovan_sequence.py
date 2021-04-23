# 파도반 수열

#n=10 [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

dp=[0,1,1,1]+[0]*97

t=int(input())
for _ in range(t):
  n=int(input())
  for i in range(3, n+1):
    if i:
      dp[i]=dp[i-3]+dp[i-2]
  print(dp[n])
