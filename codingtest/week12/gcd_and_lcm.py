# 최대공약수와 최소공배수

#24 18
n, m=map(int, input().split())

lcm=n*m
while n!=m:
  if n>m:
    n-=m
  else:
    m-=n
gcd=m
lcm//=gcd

print(gcd)
print(lcm)
