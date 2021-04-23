# 무지의 먹방 라이브
# 난이도 1
# 풀이시간 13분/30분

##책에 나온 예제는 풀었지만 프로그래머스 케이스 테스트에서 실패

food_times=[3, 1, 2]
k=5

data=food_times
for i in range(k):
  data[i%len(data)]-=1
  if data[i%len(data)]==0:
    data.pop(i%len(data))
answer = len(data)
if len(data)==0:
  answer=-1
print(answer)