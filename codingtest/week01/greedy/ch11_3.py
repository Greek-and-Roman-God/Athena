# 문자열 뒤집기
# 난이도 1
# 풀이시간 27분/20분

#틀림
import math

data=list(input())
pre=data[0]
cnt=0

for temp in data[1:]:
  if pre!=temp:
    cnt+=1
  pre=temp

result=math.ceil(cnt/2)
print(result)
