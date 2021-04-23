# 두 배열의 원소 교체

n,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
  a.append(b.pop(0))
  b.append(a.pop(0))

print(sum(a))