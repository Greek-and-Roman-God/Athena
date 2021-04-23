#상하좌우
#난이도 1
#풀이 시간 16분/15분

n=int(input())
data=list(input().split())

result=[1,1]

for c in data:
  if c=="U":
    result[0]-=1
    if result[0]<1 : result[0]=1
  elif c=="D":
    result[0]+=1
    if result[0]>n : result[0]=5
  elif c=="L":
    result[1]-=1
    if result[1]<1 : result[1]=1
  else :
    result[1]+=1
    if result[1]>n : result[1]=n

print(result)
