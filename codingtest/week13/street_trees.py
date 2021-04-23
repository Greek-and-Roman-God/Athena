# 가로수

# 4
# 1
# 3
# 7
# 13
#2, 6, 12, 18

n=int(input())
trees=[int(input()) for _ in range(n)]
gcd=trees[1]-trees[0]
for i in range(2,n):
  g=trees[i]-trees[i-1]
  while g:
    temp=gcd%g
    gcd=g
    g=temp

cnt=(trees[-1]-trees[0])//gcd-(n-1)
print(cnt)
