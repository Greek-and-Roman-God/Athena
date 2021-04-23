#수 찾기

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
n=int(input())
a=list(map(int, input().split()))
m=int(input())
search_num_list=list(map(int, input().split()))

a.sort()

for search_num in search_num_list:
  start_idx=0
  end_idx=len(a)-1
  center_idx=len(a)//2
  while True:
    if a[center_idx]==search_num:
      print(1)
      break
    if a[center_idx]<search_num:
      start_idx=center_idx+1
    else:
      end_idx=center_idx-1
    center_idx=(start_idx+end_idx)//2
    if start_idx>end_idx:
      print(0)
      break