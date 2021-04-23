# 베르트랑 공준

prime=[True]*(123456*2)
prime[0]=False
prime[1]=False

end=int((123456*2)**0.5)+1
for i in range(2,end):
  if prime[i]==True:
    for j in range(i+i, 123456*2, i):
      prime[j]=False

answer=[]
while True:
  n=int(input())
  if not n: break
  print(prime[n+1:n*2+1].count(True))
