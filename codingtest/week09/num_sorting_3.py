# 수 정렬하기 3

import sys
n = int(sys.stdin.readline())
numbers = [0]*10001
for _ in range(n):
  numbers[int(sys.stdin.readline())]+=1

for i in range(len(numbers)):
  if numbers[i]!=0:
    for _ in range(numbers[i]):
      print(i)
