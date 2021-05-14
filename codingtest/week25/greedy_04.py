# 만들 수 없는 금액

n=int(input())
coins=list(map(int, input().split()))

ans=1

for c in coins:
    if ans<c:
        break
    ans+=c

print(ans)