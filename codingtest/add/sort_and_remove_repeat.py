# 중복 빼고 정렬하기
# https://www.acmicpc.net/problem/10867


# 10
# 1 4 2 3 1 4 2 3 1 2

n=int(input())
nums=list(set(list(map(int,input().split()))))
nums.sort()

print(*nums)