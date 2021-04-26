# 평균
# https://www.acmicpc.net/problem/1546

n=int(input())
nums=list(map(int, input().split()))

max_num=max(nums)
for i in range(n):
    nums[i]=nums[i]/max_num*100
print(sum(nums)/n)