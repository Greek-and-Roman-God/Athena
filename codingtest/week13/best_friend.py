# 환상의 짝꿍

n=2*(10**6)
temp=[True]*(n+1)
end=round(n**0.5)+1
for i in range(2,end):
  if temp[i]:
    for j in range(i+i, n+1, i):
      temp[j]=False
prime=[i for i in range(2, n) if temp[i]]

def is_prime(n):
  if n>=2*(10**6):
    for p in prime:
      if n%p==0:
        return False
    return True
  else:
    return temp[n]

t=int(input())

for _ in range(t):
  a,b=map(int,input().split())
  hap=a+b
  if hap<4:
    print("NO")
    continue
  if hap%2==0: #골드바흐의 추측
    print("YES")
    continue
  if is_prime(hap-2): #홀수=홀수+짝수
    print("YES")
  else:
    print("NO")