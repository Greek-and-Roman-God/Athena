# 소수 구하기

m, n=map(int, input().split())

end=int(n**0.5)+1
temp_list=[True]*(n+1)
temp_list[0]=False
temp_list[1]=False

for i in range(2,end):
  if temp_list[i]==True:
    for j in range(i+i, n+1, i):
      temp_list[j]=False

for i in range(m,n+1):
  if temp_list[i]==True:
    print(i)