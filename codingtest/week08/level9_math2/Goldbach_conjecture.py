# 골드바흐의 추측

#시간초과
#시간초과가 나온 이유
#나는 주어진 수 (n) 의 중간부터 하나 위로 올라가면서 소수를 만나면, 그 소수부터 다시 하나씩 내려가면서 소수를 만났을 때 매번 더하고, 그 값이 n과 같은지를 검사했는데,
#n의 중간부터 값을 하나씩 내려가면서 (올라가도 될 듯) 그 수가 소수라면 n에서 그 소수를 뺀 수도 소수인지 검사하는게 훨씬 효율적임....

prime=[True]*(10000+1) # 최댓값을 5000으로 해도됨 (입력값의 최대가 10000이라면 5000+5000 이 최대일 수 있기 때문)
prime[0]=prime[1]=False
end=int((10000+1)**0.5)+1

for i in range(end):
  if prime[i]:
    for j in range(i+i,10000+1,i):
      prime[j]=False

t=int(input())

for _ in range(t):
  n=int(input())
  temp=n//2
  for i in range(temp, 1, -1):
    if prime[i] and prime[n-i] :
      print(f'{i} {n-i}')
      break

