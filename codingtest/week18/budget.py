# 예산
# https://www.acmicpc.net/problem/2512

# 4
# 120 110 140 150
# 485

n=int(input())
n_nums=list(map(int, input().split()))
m=int(input())

if sum(n_nums)<=m:
  print(max(n_nums))
  exit()

start=m//n
end=max(n_nums)
center=(start+end)//2
while start<=end:
  hap=0
  for i in n_nums:
    temp=i
    if i>center:
      temp=center
    hap+=temp
  if hap<=m:
    start=center+1
  else:
    end=center-1
  center=(start+end)//2
    
print(center)