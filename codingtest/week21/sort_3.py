# 성적이 낮은 순서로 학생 출력하기

n=int(input())
stu=[list(input().split()) for _ in range(n)]
stu.sort(key=lambda x: x[1])

for n,_ in stu:
  print(n, end='')