# 나무 자르기
# https://www.acmicpc.net/problem/2805

# 4 7
# 20 15 10 17

# Python3는 시간초과, PyPy3 로 통과
n,m=map(int,input().split())
trees=list(map(int, input().split()))

max_tree=max(trees)
start=0
end=max_tree
center=(start+end)//2
answer=0
while start<=end:
  hap=0
  center=(start+end)//2
  for tree in trees:
    if tree-center>0:
      hap+=tree-center
  if hap>=m:
    start=center+1
    answer=center
  elif hap<m:
    end=center-1

print(answer)