# 소수의 연속합

n=int(input())

temp=[True]*(n+1)
end=round(n**0.5)+1
for i in range(2,end):
  if temp[i]:
    for j in range(i+i, n+1, i):
      temp[j]=False

prime=[i for i in range(2, n+1) if temp[i]]

cnt=0
for i in range(len(prime)):
  seq_sum=0
  idx=i
  while seq_sum<=n and idx<=len(prime):
    if seq_sum==n:
      cnt+=1
      break
    if idx==len(prime):
      break
    seq_sum+=prime[idx]
    idx+=1

print(cnt)