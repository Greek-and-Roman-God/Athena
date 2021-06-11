# 공유기 설치

n,c=map(int, input().split())
ns=[int(input()) for _ in range(n)]
ns.sort()

start=ns[1]-ns[0]
end=ns[-1]-ns[0]
result=0

while start<=end:
    mid=(start+end)//2

    temp=ns[0]
    cnt=1
    for i in range(1, n):
        if ns[i]>=temp+mid:
            temp=ns[i]
            cnt+=1
    if cnt>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)
