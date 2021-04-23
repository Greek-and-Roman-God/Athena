# 소인수분해

n=int(input())

div=2
while n>1:
  if n%div==0:
    n//=div
    print(div)
    continue
  div+=1