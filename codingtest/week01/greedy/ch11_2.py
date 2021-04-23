# 곱하기 혹은 더하기
# 난이도 1
# 풀이시간 12분/30분

#틀림 (수정 완)

data=input()

result=data[0]
for i in range(1,len(data)):
  num=int(data[i])
  if num<2 and result<2:
    result+=num
  else:
    result*=num
print(result)