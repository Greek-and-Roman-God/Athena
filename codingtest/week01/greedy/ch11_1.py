# 모험가 길드
# 난이도 1
# 풀이시간 18분/30분

#틀림

n=input()
data=list(map(int, input().split()))
data.sort()
cnt=0
while len(data)>0:
  length=len(data)
  num=data[length-1]
  for i in range(num):
    data.pop(length-1-i)
  cnt+=1
print(cnt)