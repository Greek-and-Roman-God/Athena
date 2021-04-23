# 1,2,3 더하기

def dfs(n, hap):
  ans=0
  if hap==n:
    ans+=1
  if hap>=n:
    return ans
  for i in range(1, 4):
    ans+=dfs(n, hap+i)
  return ans

t=int(input())
#3
#4 7 10
for _ in range(t):
  n=int(input())
  ans=0
  for i in range(1,4):
    ans+=dfs(n, i)
  print(ans)
