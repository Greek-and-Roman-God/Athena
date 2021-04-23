# 큰수의 법칙
import time

n, m, k=map(int, input().split())
nums=list(map(int, input().split()))

start_t=time.time()

nums.sort()

div=m//(k+1)
remain=m%(k+1)
ans=nums[-1]*((div*k)+remain)+nums[-2]*(div)
print(ans)

print(time.time()-start_t)