# 에디터
# https://www.acmicpc.net/problem/1406

# abcd
# 3
# P x
# L
# P y
import sys

stack1=list(sys.stdin.readline().rstrip())
stack2=[]
cursor=len(stack1)
for _ in range(int(sys.stdin.readline())):
  comm=sys.stdin.readline().rstrip().split()
  if comm[0]=="L":
    if stack1:
      stack2.append(stack1.pop())
  elif comm[0]=="D":
    if stack2:
      stack1.append(stack2.pop())
  elif comm[0]=="B":
    if stack1:
      stack1.pop()
  else:
    stack1.append(comm[1])

print("".join(stack1+stack2[-1::-1]))