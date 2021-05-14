# 뱀

n=int(input())
k=int(input())
data=[[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b=map(int, input().split())
    datat=[a][b]=1

l=int(input())
info=[]
for _ in range(l):
    x,c=input().split()
    info.append((int(x), c))
