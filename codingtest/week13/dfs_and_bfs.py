# DFS와 BFS
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

def dfs(v, n, matrix, check):
  check[v]=True
  print(v, end=' ')
  for i in range(1,n+1):
    if not check[i] and matrix[v][i]==1:
      dfs(i, n, matrix, check)

def bfs(v, n, matrix, check):
  queue=[v]
  check[v]=True
  while queue:
    v=queue.pop(0)
    print(v, end=' ')
    for i in range(1, n+1):
      if not check[i] and matrix[v][i]==1:
        queue.append(i)
        check[i]=True

n, m, v=map(int, input().split())
matrix=[[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a,b=map(int, input().split())
  matrix[a][b] = 1
  matrix[b][a] = 1

dfs(v, n, matrix, [False]*(n+1))
print()
bfs(v, n, matrix, [False]*(n+1))
