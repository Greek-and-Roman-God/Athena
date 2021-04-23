# 숫자 카드 게임

n,m=map(int, input().split())

nums=[] #각 행에서 가장 작은 수만 저장하는 리스트
for _ in range(n):
  nums.append(min(list(map(int, input().split()))))
print(max(nums))