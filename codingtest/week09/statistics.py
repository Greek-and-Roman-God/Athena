# 통계학

# 5
# 1
# 3
# 8
# -2
# 2
import sys
from collections import Counter

n=int(sys.stdin.readline())
numbers=[]
for _ in range(n):
  numbers.append(int(sys.stdin.readline()))
numbers.sort()

arithmetic_mean=round(sum(numbers)/len(numbers)) #산술평균
median=numbers[round(n/2)] #중앙값
scale=numbers[-1]-numbers[0] #범위

num_cnt = Counter(numbers).most_common()
mode=num_cnt[0][0] #최빈값
if len(num_cnt)>1 and num_cnt[0][1]==num_cnt[1][1]:
  mode=num_cnt[1][0]

print(arithmetic_mean)
print(median)
print(mode)
print(scale)