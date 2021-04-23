# 분수찾기

x=int(input())

cnt=0
while x>0:
  cnt+=1
  x-=cnt
remain=cnt+x

if cnt%2==1: #cnt가 홀수면 오른쪽 대각선 위로 올라가야함
  #cnt/1 부터 1/cnt의 순서로 바뀌어야 함
  print(f'{cnt-remain+1}/{remain}')
else : #cnt가 짝수면 왼쪽 대각선 아래로 내려가야함
  print(f'{remain}/{cnt-remain+1}')
