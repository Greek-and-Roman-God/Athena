# 피보나치 함수

t=int(input())

for _ in range(t):
  n=int(input())
  cnt_0=[1,0]+[0]*(n-1)
  cnt_1=[0,1]+[0]*(n-1)
  for i in range(2,n+1):
    cnt_0[i]=cnt_0[i-2]+cnt_0[i-1]
    cnt_1[i]=cnt_1[i-2]+cnt_1[i-1]
  print(f'{cnt_0[n]} {cnt_1[n]}')