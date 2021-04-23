# 소수 찾기

n=4
num=[1,3,5,7]
#n=int(input())
#num=list(map(int,input().split()))

temp_list=[True]*1000

end=int(1000**0.5)+1
for i in range(2, end):
  if temp_list[i]==True:
    for j in range(i+i, 1000, i):
      temp_list[j]=False

prime=list(i for i in range(2, 1000) if temp_list[i]==True)

cnt=0
for temp in num:
  if temp in prime:
    cnt+=1
print(cnt)