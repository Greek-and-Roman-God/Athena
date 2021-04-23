# 연속합
# https://www.acmicpc.net/problem/1912


# n=10
# n_list=[10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

# 10
# 2 1 -4 3 4 -4 6 5 -5 1

# 5
# -1 -2 -3 -4 -5

n=int(input())
n_list=list(map(int, input().split()))

dp=[0]*n
dp[0]=n_list[0]
max_num=dp[0]
for i in range(1,n):
  dp[i]= max(dp[i-1]+n_list[i], n_list[i])
  max_num= max(dp[i],max_num)

print(max_num)