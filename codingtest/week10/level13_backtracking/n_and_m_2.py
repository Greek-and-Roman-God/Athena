# N과 M (2)

# 처음 코드 - 출력 초과
# def dfs(nums, m, ans, depth):
#   if m==depth:
#     print(ans)
#     return
#   for n in nums:
#     if str(n) in ans:
#       continue
#     dfs(nums, m, ans+" "+str(n), depth+1)
#   return

# def call_dfs(n, m):
#   nums=[]
#   for i in range(1,n+1):
#     nums.append(i)
#   if n!=m:
#     while nums:
#       dfs(nums, m, str(nums[0]), 1)
#       nums.pop(0)
#   else:
#     answer=str(nums[0])
#     for num in nums[1:]:
#       answer=answer+" "+str(num)
#     print(answer)
#   return

# n, m=map(int,input().split())
# call_dfs(n, m)

# 구글 코드
# def dfs(depth, n, m, nums, check, ans):
#   if depth==m:
#     print(*ans)
#     return
#   for i in range(n):
#     if check[i]: continue
#     ans.append(nums[i])
#     check[i]=True
#     dfs(depth+1, n, m, nums, check, ans)
#     ans.pop()
#     for j in range(i+1, n):
#       check[j]=False

# n,m=map(int, input().split())
# nums=[i for i in range(1, n+1)]
# check=[False]*n
# ans=[]
# dfs(0, n, m, nums, check, ans)

#210118 수정
# def dfs(n, m, check, ans):
#   if len(ans)==m:
#     print(*ans)
#     return
#   for i in range(n):
#     if check[i]: continue
#     ans.append(i+1)
#     check[i]=True
#     dfs(n, m, check, ans)
#     ans.pop()
#     for j in range(i+1, n):
#       check[j]=False

# n,m=map(int, input().split())
# check=[False]*n
# ans=[]
# dfs(n, m, check, ans)

#210118 추가
def dfs(n, m, check, ans, cnt):
  if len(ans)==m:
    print(*ans)
    return
  for i in range(cnt,n):
    if check[i]: continue
    ans.append(i+1)
    check[i]=True
    dfs(n, m, check, ans, i+1)
    ans.pop()
    check[i]=False

n,m=map(int, input().split())
check=[False]*n
ans=[]
dfs(n, m, check, ans, 0)