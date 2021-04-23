# 약수

# n=2
# divisor=[4, 2]

n=int(input())
divisor=list(map(int, input().split()))

divisor.sort()
print(divisor[0]*divisor[-1])