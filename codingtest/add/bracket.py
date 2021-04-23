# 괄호
# https://www.acmicpc.net/problem/9012

# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

from collections import deque

t=int(input())
for _ in range(t):
  bracket=input()
  stack=deque()
  answer="YES"
  for b in bracket:
    if b=="(":
      stack.append(b)
      continue
    if not stack or stack.pop()!="(":
      answer="NO"
      break
  else:
    if stack:
      answer="NO"
  print(answer)
