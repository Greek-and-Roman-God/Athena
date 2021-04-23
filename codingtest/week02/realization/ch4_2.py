#시각
#난이도 1
#풀이 시간 30분/15분


n=int(input())

cnt_per_hour=(15*9+60)*5+60*10 #한 시간마다 3이 들어가는 횟수
result=0

for i in range(n+1):
  list=[]
  for c in str(i):
    list.append(int(c))
  if 3 in list : #if 3 in str(i) 로 줄일 수 있음
    result+=60*60 #시간에 3이 들어가는 경우 모든 분/초를 세기
    continue
  result+=cnt_per_hour

print(result)