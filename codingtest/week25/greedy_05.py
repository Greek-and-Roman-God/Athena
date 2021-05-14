#  볼링공 고르기

n, m=map(int, input().split())
k=list(map(int, input().split()))

arr=[0]*(m+1)

for i in k:
    arr[k]+=1

ans=0
for i in range(1, m+1):
    n-=arr[i]
    ans+=arr[i]*n

print(ans)