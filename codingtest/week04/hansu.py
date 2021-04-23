#한수

def solve(n:int)->int:
  if n<100:
    cnt=n
    return cnt
  else:
    cnt=99
  for num in range(100,n+1):
    num1=num%10
    num//=10
    num2=num%10
    num//=10
    step=num1-num2
    while num>0:
      num1=num2
      num2=num%10
      num//=10
      if step!=(num1-num2):
        cnt-=1
        break
    cnt+=1
  return cnt
n=int(input())
print(solve(n))