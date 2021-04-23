# 큐
# https://www.acmicpc.net/problem/10845

# 15
# push 1
# push 2
# front
# back
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
# front


import sys

n=int(sys.stdin.readline().rstrip())

queue=[0]*n
front=0
end=0
for _ in range(n):
  comm=sys.stdin.readline().rstrip().split()
  if comm[0]=="push":
    queue[end]=comm[1]
    end+=1
  elif comm[0]=="pop":
    if front!=end:
      print(queue[front])
      front+=1
    else:
      print(-1)
  elif comm[0]=="front":
    if front!=end:
      print(queue[front])
    else:
      print(-1)
  elif comm[0]=="back":
    if front!=end:
      print(queue[end-1])
    else:
      print(-1)
  elif comm[0]=="size":
    print(end-front)
  elif comm[0]=="empty":
    if front!=end:
      print(0)
    else:
      print(1)