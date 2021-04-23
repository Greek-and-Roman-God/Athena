# AC
# https://www.acmicpc.net/problem/5430

# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []

t=int(input())

for _ in range(t):
  comm=input()
  n=int(input())
  nums=[]
  if n:
    nums=list(input()[1:-1].split(","))
  else:
    input()
  
  is_reverse=False
  front=0
  rear=n
  for c in comm:
    if c=="R":
      is_reverse= not is_reverse
    if c=="D":
      if is_reverse:
        rear-=1
      else:
        front+=1
  if front>rear:
    print("error")
    continue
  ans=[]
  if is_reverse:
    for i in range(rear-1, front-1, -1):
      ans.append(nums[i])
  else:
    for i in range(front, rear):
      ans.append(nums[i])
  print("["+",".join(ans)+"]")

