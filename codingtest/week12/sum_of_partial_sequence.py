# 부분수열의 합

# n, s=5, 0
# nums=[-7, -3, -2, 5, 8]

n, s=map(int, input().split())
nums=list(map(int, input().split()))

def dfs(n, s, nums, check, depth, hap):
  ans=0
  if depth>0 and hap==s:
    ans+=1
  if depth==n:
    return ans
  for i in range(n):
    if check[i]: continue
    check[i]=True
    ans+=dfs(n, s, nums, check, depth+1, hap+nums[i])
    for j in range(i+1, n):
      check[j]=False
  return ans

check=[False]*n
ans=dfs(n, s, nums, check, 0, 0)
print(ans)