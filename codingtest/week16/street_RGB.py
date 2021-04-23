# RGB거리

# 3
# 26 40 83
# 49 60 57
# 13 89 99

n=int(input())
dp=list(map(int, input().split()))
for _ in range(n-1):
  temp=list(map(int, input().split()))
  for i in range(3):
    temp[i]+=min(dp[:i]+dp[i+1:])
  dp=temp[:]
print(min(dp))