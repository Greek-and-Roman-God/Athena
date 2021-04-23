#랜선자르기

# n=4
# m=11
# lines=[802, 743, 457, 539]
n, m=map(int, input().split())
lines=[]
for i in range(n):
  lines.append(int(input()))

max_line=max(lines)

start=1
end=max_line
center=(start+end)//2

while True:
  cnt=0
  for line in lines:
    cnt+=line//center
  if cnt==m:
    while True:
      cnt=0
      start=center
      center=(start+end)//2
      for line in lines:
        cnt+=line//center
      if cnt==m:
        end=center
        center=(start+end)//2
      print(center)
    break
  elif cnt>m:
    start=center+1
    center=(start+end)//2
  else:
    end=center-1
    center=(start+end)//2
  if start>end:
    break

print(center)