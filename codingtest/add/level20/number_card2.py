#숫자 카드2

n=10
a=[6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
m=8
b=[10, 9, -5, 2, 3, 4, 5, -10]
# n=int(input())
# a=list(map(int, input().split()))
# m=int(input())
# b=list(map(int, input().split()))

a.sort()
dic={}
for num in a:
  if num in dic:
    dic[num]=dic[num]+1
  else:
    dic[num]=1

for search_num in b:
  start_idx=0
  end_idx=len(a)-1
  center_idx=len(a)//2
  while True:
    if a[center_idx]==search_num:
      print(dic[search_num])
      break
    if a[center_idx]<search_num:
      start_idx=center_idx+1
    else:
      end_idx=center_idx-1
    center_idx=(start_idx+end_idx)//2
    if start_idx>end_idx:
      print(0)
      break