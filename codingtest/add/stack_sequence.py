# 스택 수열
# https://www.acmicpc.net/problem/1874

# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

n=int(input())
n_nums=[0]*n
for i in range(n):
  n_nums[i]=int(input())

stack=[]
process=[]
idx=0
for i in range(1,n+1):
  stack.append(i)
  process.append("+")
  while stack and idx<n:
    temp=stack.pop()
    if  n_nums[idx]!=temp:
      stack.append(temp)
      break
    process.append("-")
    idx+=1
if stack:
  print("NO")
else:
  for p in process:
    print(p)
    
  
  