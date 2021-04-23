#나이순 정렬

# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

n=int(input())
mem_list=[]
for _ in range(n):
  mem_list.append(list(input().split()))

mem_list=sorted(mem_list, key=lambda x: int(x[0]))

for age, name in mem_list:
  print(f'{age} {name}')