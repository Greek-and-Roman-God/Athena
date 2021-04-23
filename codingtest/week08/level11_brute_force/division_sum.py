# 분해합

# n=int(input())
# ans_list=[]
# num_sum=0
# # for의 범위를 216-(9*3) 부터 216까지 도는걸로 하는게 더 좋음
# for i in range(n):
#   num=str(i)
#   num_sum=i
#   for j in num:
#     num_sum+=int(j)
#   if num_sum==n:
#     ans_list.append(i)
# ans_list.append(0)
# print(ans_list[0])
# print(ans_list)

#혜린언니 코드 응용
n=int(input())
answer=0
num_sum=0
num_len=len(str(n))
start=n-(9*num_len)
for i in range(start, n):
  num=str(i)
  num_sum=i
  for j in num:
    num_sum+=int(j)
  if num_sum==n:
    answer=i
    break
print(answer)