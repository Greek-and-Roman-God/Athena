# 스택
# https://www.acmicpc.net/problem/10828

# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top
import sys

n=int(sys.stdin.readline().rstrip())

stack=[0]*n
top=-1
for _ in range(n):
  comm=sys.stdin.readline().rstrip().split()
  if comm[0]=="push":
    top+=1
    stack[top]=comm[1]
  elif comm[0]=="pop":
    if top!=-1:
      print(stack[top])
      top-=1
    else:
      print(-1)
  elif comm[0]=="top":
    if top!=-1:
      print(stack[top])
    else:
      print(-1)
  elif comm[0]=="size":
    print(top+1)
  elif comm[0]=="empty":
    if top!=-1:
      print(0)
    else:
      print(1)
  