# N-Queen

n=int(input())
ans=0
ver=[False]*n
dia_right=[False]*(n*2-1)
dia_left=[False]*(n*2-1)

def n_queen(i):
  global ans
  if i==n:
    ans+=1
    return
  for j in range(n):
    if not (ver[j] or dia_right[i+j] or dia_left[i-j+n-1]):
      ver[j] = dia_right[i+j] = dia_left[i-j+n-1] = True
      n_queen(i+1)
      ver[j] = dia_right[i+j] = dia_left[i-j+n-1] = False
  return ans

print(n_queen(0))