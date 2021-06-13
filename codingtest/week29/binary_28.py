# 고정점 찾기

n=int(input())
ns=list(map(int, input().split()))

fixed_point=-1

start, end=0, n-1
while start<=end:
    mid=(start+end)//2
    if ns[mid]==mid:
        fixed_point=mid
        break
    if ns[mid]>mid:
        end=mid-1
    if ns[mid]<mid:
        start=mid+1

print(fixed_point)
