# N과 M (3)

# 풀이1
# def dfs(nums, m, ans, depth):
#   if m==depth:
#     print(ans)
#     return
#   for n in nums:
#     # if str(n) in ans:
#     #   continue
#     dfs(nums, m, ans+" "+str(n), depth+1)
#   return

# def call_dfs(n, m):
#   nums=[]
#   for i in range(1,n+1):
#     nums.append(i)
#   for n in nums:
#     dfs(nums, m, str(n), 1)
#   return

# n,m = map(int, input().split())
# call_dfs(n, m)

# 풀이2
# def dfs(n, m, nums, ans):
#   if len(ans)==m:
#     print(" ".join(map(str, ans)))
#     return
#   for i in range(n):
#     ans.append(nums[i])
#     dfs(n, m, nums, ans)
#     ans.pop()
#   return

# n,m=map(int, input().split())
# nums=[i for i in range(1, n+1)]
# ans=[]
# dfs(n, m, nums, ans)

#210118 추가
def dfs(n, m, ans):
  if len(ans)==m:
    print(" ".join(map(str, ans)))
    return
  for i in range(n):
    ans.append(i+1)
    dfs(n, m, ans)
    ans.pop()
  return

n,m=map(int, input().split())
ans=[]
dfs(n, m, ans)