# 골드바흐의 추측

prime=[True]*1000001
end=round(1000001**0.5)+1
for i in range(2,end):
  if prime[i]:
    for j in range(i+i, 1000001, i):
      prime[j]=False

n=int(input())
while n!=0:
  for i in range(2,n//2+1):
    if prime[i] and prime[n-i]==n:
      print(f'{n} = {i} + {n-i}')
      break
  else:
    print("Goldbach's conjecture is wrong.")
  n=int(input())
