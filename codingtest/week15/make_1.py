# 1로 만들기

# 1,2,3의 경우는 011
# 2나 3으로 나누어지면 나눈 후의 값을 찾아서 더하기
# 안나누어지면  1을뺀뒤 그 값을 더하기

n=int(input())
dp=[0,0,1,1]+[0]*(n-3)

for x in range(4,n+1):
  temp=0
  if not x%3:
    temp=dp[x//3]+1
  if not x%2:
    temp=temp if temp and dp[x//2]+1>temp else dp[x//2]+1
  dp[x]=temp if temp and dp[x-1]+1>temp else dp[x-1]+1
print(dp[n])
print(dp)