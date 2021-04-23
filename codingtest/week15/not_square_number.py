# 제곱 ㄴㄴ수

import math

results = []
min_num, max_num = map(int, input().split())
validation = [1 for _ in range(min_num, max_num+1)] 

search_target = int(math.sqrt(max_num))
squares = [v**2 for v in range(2, search_target+1)]
for square in squares:
  cur_idx = (math.ceil(min_num / square) * square) - min_num
  while cur_idx <= max_num - min_num:
    validation[cur_idx] = 0
    cur_idx += square

result = sum(validation)
print(result)
