#왕실의 나이트
#난이도 1
#풀이 시간 16분/20분

cur=list(input()) #현재 위치
#list는 책 풀이 참고
list=[(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
cnt=0

for set in list:
  x=ord(cur[0])+set[0]
  y=int(cur[1])+set[1]
  if x>96 and x<105 and y>0 and y<9:
    cnt+=1

print(cnt)