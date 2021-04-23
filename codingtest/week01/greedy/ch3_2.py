n, m, k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
result=0
lastIdx=n-1
cnt=1

#틀린 코드 if문의 조건이 이상함!
for i in range(1,m+1):
  
  if i==k*cnt+1:
    result+=data[lastIdx-1]
    cnt+=1
  else :
    result+=data[lastIdx]
  print(result)

print(result)

## 책 답안
count = m//(k+1) * k + m%(k+1)
result1= data[lastIdx]*count + data[lastIdx-1]*(m-count)
print(result1)