# 좋은 수열

def bt(n, s, idx):
  for i in range(1, (idx//2) + 1):
    if s[-i:] == s[-2*i:-i]:
      return -1
  if idx == n:
    print(int(''.join(map(str,s))))
    return 0
  for i in range(1, 4):
    s.append(i)
    if bt(n, s, idx + 1) == 0:
      return 0
    s.pop()

n=int(input())
s=[]
bt(n, s, 0)