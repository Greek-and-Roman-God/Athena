# 덩치

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

n=int(input())

phy_list=[]
for _ in range(n):
  x, y=map(int,input().split())
  phy_list.append([x,y])

rank=[1]*n
for idx,phy in enumerate(phy_list):
  for phy2 in phy_list[:idx]+phy_list[idx+1:]:
    if phy[0]<phy2[0] and phy[1]<phy2[1]:
      rank[idx]+=1
print(rank)
for r in rank:
  print(r, end=" ")
print()