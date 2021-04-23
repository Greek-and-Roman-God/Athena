#손익분기점

a, b, c=map(int,input().split())

#시간초과
# if b>=c:
#   print(-1)
# else:
#   bep=1
#   while a+b*bep >= c*bep:
#     bep+=1
#   print(bep)

if b>=c:
  print(-1)
else:
  print(a//(c-b)+1)