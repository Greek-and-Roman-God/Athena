# 로또

def dfs(k, s, check, ans):
  if len(ans)==6:
    print(*ans)
    return
  for i in range(k):
    if check[i]: continue
    check[i]=True
    ans.append(s[i])
    dfs(k, s, check, ans)
    ans.pop()
    for j in range(i+1, k):
      check[j]=False

tk=[]
while True:
  s=list(map(int, input().split()))
  k=s.pop(0)
  if not s:
    break
  tk.append([k,s])
for k, s in tk:
  check=[False]*k
  ans=[]
  dfs(k, s, check, ans)
  print()
  


# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0
