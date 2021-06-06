# 정렬된 배열에서 특정 수의 개수 구하기

n, x=map(int, input().split())
ns=list(map(int, input().split()))

first, last=-1,n

start, end=0, n-1
while start<=end:
    mid=(end+start)//2
    if ns[mid]==x:
        end=mid-1
        first=mid
        continue
    if ns[mid]>x:
        end=mid-1
    if ns[mid]<x:
        start=mid+1

if first==-1:
    print(-1)
else:
    start, end=first, n-1
    while start<=end:
        mid=(end+start)//2
        if ns[mid]==x:
            start=mid+1
            last=mid
            continue
        if ns[mid]>x:
            end=mid-1
        if ns[mid]<x:
            start=mid+1
    print(last-first+1)