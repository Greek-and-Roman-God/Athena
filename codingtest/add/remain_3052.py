# 나머지
# https://www.acmicpc.net/problem/3052

nums=[]
for _ in range(10):
    nums.append(int(input())%42)
print(len(set(nums)))