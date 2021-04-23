#셀프 넘버


def solve():
  nums=list(range(1,100))
  answer=nums[:]
  for num in nums:
    i=num
    temp=i
    while i>0:
      temp+=i%10
      i//=10
    if temp in answer:
      answer.remove(temp)
  for ans in answer:
    print(ans)

solve()
