# 볼링공 고르기
# 난이도 1
# 풀이시간 8분/30분
n, m=map(int, input().split())
data=list(map(int, input().split()))
cnt=0
for i in range(len(data)):
  for j in range(i+1,len(data)):
    if data[i]!=data[j]:
      cnt+=1
print(cnt)

#도연이 코드
#기준이 되는 값 외에 조합이 될 수 있는 모든 수에서 중복값을 제외하는 방식으로 풀면 for문을 한번만 쓸 수 있다 (factorial개념 응용, list의 count함수 사용)