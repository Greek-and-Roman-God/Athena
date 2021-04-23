#부녀회장이 될테야

t=int(input())

for _ in range(t):
  k=int(input())
  n=int(input())
  apartment=[]
  for i in range(k+1):
    apartment.append([0]*n)
  for i in range(len(apartment[0])):
    apartment[0][i]=i+1
  for idx,temp in enumerate(apartment):
    print(f'{idx} {temp}')
    if idx==0:
      continue
    apartment[idx][0]=1
    for j in range(1,len(temp)):
      apartment[idx][j]=apartment[idx][j-1]+apartment[idx-1][j]
  print(apartment[-1][-1])


