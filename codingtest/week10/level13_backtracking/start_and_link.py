# 스타트와 링크

def dfs(n, s, depth, check, cnt, ans):
  if depth==n//2:
    start, link=[],[]
    s_sum, l_sum=0,0
    for idx, flag in enumerate(check):
      #print(f'{idx} {flag}')
      if flag: #True면 start팀
        start.append(idx)
      else:
        link.append(idx)
    for x in range(n//2):
      for y in range(n//2):
        s_sum+=s[start[x]][start[y]]
        l_sum+=s[link[x]][link[y]]
    ans.append(abs(s_sum-l_sum))
    return
  for i in range(cnt,n):
    if check[i]: continue
    check[i]=True
    cnt+=1
    dfs(n, s, depth+1, check, cnt, ans)
    check[i]=False
    print()

def call_dfs(n,s):
  check=[False]*n
  ans=[]
  cnt=1 
  depth=1
  check[0]=True
  dfs(n, s, depth, check, cnt, ans)
  return min(ans)

n=int(input())
s=[]
for _ in range(n):
  s.append(list(map(int, input().split())))

# n=4
# s=[[0, 1, 2, 3],[4, 0, 5, 6],[7, 1, 0, 2],[3, 4, 5, 0]]

# n=6
# s=[[0, 1, 2, 3, 4, 5],[1, 0, 2, 3, 4, 5],[1, 2, 0, 3, 4, 5],[1, 2, 3, 0, 4, 5],[1, 2, 3, 4, 0, 5],[1, 2, 3, 4, 5, 0]]
print(call_dfs(n,s))
