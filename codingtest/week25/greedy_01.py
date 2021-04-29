# 모험가 길드

n=int(input())
ns=list(map(int, input().split()))

ns.sort()
ans=0
cnt=0
for i in ns:
    cnt+=1
    if i<=cnt:
        cnt=0
        ans+=1

print(ans)