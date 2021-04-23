# 숫자 카드

# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

n=int(input())
n_list=list(map(int, input().split()))
n_list.sort()

m=int(input())
m_list=list(map(int, input().split()))

for x in m_list:
  s,e,c=0, n-1, n//2
  while True:
    if x==n_list[c]:
      print(1, end=" ")
      break
    if x>n_list[c]:
      s=c+1
    else:
      e=c-1
    c=(s+e)//2
    if s>e:
      print(0, end=" ")
      break
      
