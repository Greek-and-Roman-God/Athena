# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

# 6
# 10 20 10 30 20 50

n=int(input())
a=list(map(int, input().split()))
dp=[0]*n
max_value=0
for i in range(n):
  for j in range(i):
    if a[i]>a[j]:
      dp[i]=max(dp[i],dp[j])
  dp[i]+=1
  max_value=max(dp[i],max_value)

print(dp)
print(max_value)