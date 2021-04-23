# 연산자 끼워넣기

import sys

# n=6
# nums=[1,2,3,4,5,6]
# plus, minus, mul, div=2,1,1,1

n=int(input())
nums=list(map(int, input().split()))
plus, minus, mul, div=map(int, input().split())

max_num=-sys.maxsize-1
min_num=sys.maxsize

# def dfs(depth, hap):
#   global max_num, min_num
#   if depth==n-1:
#     max_num=max(max_num, hap)
#     min_num=min(min_num, hap)
#     return
#   for i in range(n-1):
#     if check[i]: continue
#     check[i]=True
#     if operator[i]=="+":
#       dfs(depth+1, hap+nums[depth])
#     elif operator[i]=="-":
#       dfs(depth+1, hap-nums[depth])
#     elif operator[i]=="*":
#       dfs(depth+1, hap*nums[depth])
#     elif operator[i]=="/":
#       dfs(depth+1, int(hap/nums[depth]))
#     check[i]=False
#   return

def dfs(depth, hap, plus, minus, mul, div):
  global max_num, min_num
  if depth==n:
    max_num=max(max_num, hap)
    min_num=min(min_num, hap)
    return
  if plus:
    dfs(depth+1, hap+nums[depth], plus-1, minus, mul, div)
  if minus:
    dfs(depth+1, hap-nums[depth], plus, minus-1, mul, div)
  if mul:
    dfs(depth+1, hap*nums[depth], plus, minus, mul-1, div)
  if div:
    dfs(depth+1, int(hap/nums[depth]), plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)
#print(ans)
print(max_num)
print(min_num)
