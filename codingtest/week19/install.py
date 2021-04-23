# 공유기 설치
# https://www.acmicpc.net/problem/2110

# 5 3
# 1
# 2
# 8
# 4
# 9

import sys

n,c=map(int, sys.stdin.readline().split())
nums=[]
for _ in range(n):
  nums.append(int(sys.stdin.readline()))
nums.sort()

start=1
end=nums[-1]-nums[0]
result=0
while start<=end:
  center=(start+end)//2
  cnt=1
  temp=nums[0]
  for i in range(1, n):
    if temp+center<=nums[i]:
      temp=nums[i]
      cnt+=1
  if cnt>=c:
    result=center
    start=center+1
  else:
    end=center-1
print(result)
