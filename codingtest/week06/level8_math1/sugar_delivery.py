#설탕 배달

n=int(input())

# cnt=n//5
# temp=n%5
# cnt+=temp//3
# if temp%3!=0:
#   cnt=n//3
#   temp=n%3
#   if n%3!=0:
#     cnt=-1
# print(cnt)

cnt=0
if n>5:
  cnt=n//5
  remain=n%5
  if remain in (1,3): #나머지가 1이나 3이면 5를 한개 줄이고 3을 두개 추가
    cnt+=1
  elif remain==2: #나머지가 2이면 5를 두개 줄이고 3을 4개 추가
    if cnt<2:
      cnt=-1
    else:
      cnt+=2
  elif remain==4:
    cnt+=2
else:
  if n==3 or n==5:
    cnt=1
  else:
    cnt=-1
print(cnt)