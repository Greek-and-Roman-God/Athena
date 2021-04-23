# 부등호
# https://www.acmicpc.net/problem/2529

# 2
# < >

def dfs(k, sign, depth, check, ans):
  global min_num, max_num
  if depth==k+1:
    temp="".join(ans)
    if min_num=="":
      min_num=temp
    max_num=temp
    return
  for i in range(10):
    if check[i]: continue
    check[i]=True
    if sign[depth-1]=="<" and ans[-1]<str(i):
      dfs(k, sign, depth+1, check, ans+[str(i)])
    if sign[depth-1]==">" and ans[-1]>str(i):
      dfs(k, sign, depth+1, check, ans+[str(i)])
    check[i]=False
  return

k=int(input())
sign=list(input().split())

min_num=""
max_num=""
check=[False]*10
for i in range(10):
  ans=[str(i)]
  check[i]=True
  dfs(k, sign, 1, check, ans)
  check[i]=False

print(max_num)
print(min_num)
