#벌집

n=int(input())

n-=1
cnt=1

while n>0:
  n-=cnt*6
  cnt+=1
print(cnt)
