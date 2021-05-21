# 안테나

n=int(input())
location=list(map(int, input().split()))

location.sort()
print(location[(n-1)//2])