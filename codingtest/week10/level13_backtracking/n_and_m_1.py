# N과 M (1)

# 처음 코드
# def dfs(nums, m, ans, depth):
#   if m==depth:#종료조건
#     print(ans)
#     return
#   for n in nums:
#     if str(n) in ans:
#       continue
#     dfs(nums, m, ans+" "+str(n), depth+1)
#   return 0

# def call_dfs(n, m): # 4 2
#   nums=[]
#   for i in range(1,n+1):
#     nums.append(i)
#   for n in nums:
#     dfs(nums, m, str(n), 1)
#   return 0

# n,m = map(int, input().split())
# call_dfs(n, m)


#구글링 한 코드

# def dfs(depth, n, m, nums, check, ans):
#   if depth==m:
#     print(*ans)
#     return
#   for i in range(n):
#     if check[i]: continue
#     ans.append(nums[i])
#     check[i]=True
#     dfs(depth+1, n, m, nums, check, ans)
#     #print(ans)
#     #print(check)
#     ans.pop()
#     check[i]=False
    

# n,m=map(int, input().split())
# nums=[i for i in range(1, n+1)]
# check=[False]*n
# ans=[]
# dfs(0, n, m, nums, check, ans)

#210118 수정
def dfs(n, m, check, ans):
  if len(ans)==m:
    print(*ans)
    return
  for i in range(n):
    if check[i]: continue
    ans.append(i+1)
    check[i]=True
    dfs(n, m, check, ans)
    ans.pop()
    check[i]=False

n,m=map(int, input().split())
check=[False]*n
ans=[]
dfs(n, m, check, ans)