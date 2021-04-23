#나무자르기


# n,m=4, 7
# trees=[20, 15, 10, 17]
n, m=map(int, input().split())
trees=list(map(int, input().split()))

# trees.sort()
# max_tree=trees[-1]
# start=1
# end=max_tree
# center=(start+end)//2
# answer=0
# while True:
#   sum=0
#   for tree in trees:
#     if tree-center>0:
#       sum+=tree-center
#   if sum==m:
#     break
#   elif sum>m:
#     start=center+1
#   else:
#     end=center-1
#   center=(start+end)//2
#   if start>end:
#     break

# answer=center

# print(answer)



max_tree=max(trees)
start=0
end=max_tree
center=(start+end)//2
answer=0
while start<end:
  sum=0
  center=(start+end)//2
  for tree in trees:
    if tree-center>0:
      sum+=tree-center
  if sum>=m:
    start=center+1
    answer=center
  elif sum<m:
    end=center-1

print(answer)