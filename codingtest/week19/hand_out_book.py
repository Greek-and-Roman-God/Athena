# 책 나눠주기
# https://www.acmicpc.net/problem/9576


# 1
# 2 3
# 1 2
# 1 2
# 1 2

# 1
# 5 5
# 2 5
# 2 5
#  2 5
#  1 2
#  1 1

# 1
# 3 3
# 1 2
# 1 3
# 1 2

import sys

t=int(sys.stdin.readline())
for _ in range(t):
  n,m=map(int, sys.stdin.readline().split())
  m_nums=[]
  for _ in range(m):
    m_nums.append(list(map(int, sys.stdin.readline().split())))
  m_nums.sort(key=lambda x:(x[1]))
  print(m_nums)
  book=[True]+[False]*n
  cnt=0
  for ms in m_nums:
    for i in range(ms[0],ms[1]+1):
      if not book[i]:
        book[i]=True
        cnt+=1
        break
  print(cnt)
