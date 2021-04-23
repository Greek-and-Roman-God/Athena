# 덱
# https://www.acmicpc.net/problem/10866

# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

import sys

n=int(sys.stdin.readline().rstrip())

m_deque=[0]*n
front=0
end=0
for _ in range(n):
  comm=sys.stdin.readline().rstrip().split()
  if comm[0]=="push_front":
    front-=1
    m_deque[front]=comm[1]
  elif comm[0]=="push_back":
    m_deque[end]=comm[1]
    end+=1
  elif comm[0]=="pop_front":
    if front!=end:
      print(m_deque[front])
      front+=1
    else:
      print(-1)
  elif comm[0]=="pop_back":
    if front!=end:
      print(m_deque[end-1])
      end-=1
    else:
      print(-1)
  elif comm[0]=="front":
    if front!=end:
      print(m_deque[front])
    else:
      print(-1)
  elif comm[0]=="back":
    if front!=end:
      print(m_deque[end-1])
    else:
      print(-1)
  elif comm[0]=="size":
    print(end-front)
  elif comm[0]=="empty":
    if front!=end:
      print(0)
    else:
      print(1)