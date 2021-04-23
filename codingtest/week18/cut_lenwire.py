# 랜선자르기
# https://www.acmicpc.net/problem/1654

# n=4
# m=11
# lines=[802, 743, 457, 539]
n, m=map(int, input().split())
lines=[]
for i in range(n):
  temp=int(input())
  lines.append(temp)

max_line=max(lines)

start=1
end=max_line
center=(start+end)//2
answer=0
while start<=end:
  cnt=0
  for line in lines:
    cnt+=line//center
  if cnt>=m:
    start=center+1
    answer=center
  else:
    end=center-1
  center=(start+end)//2

print(answer)