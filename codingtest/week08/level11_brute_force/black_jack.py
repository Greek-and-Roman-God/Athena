# 블랙잭

n, m=map(int, input().split())
cards=list(map(int,input().split()))

sum_list=[0]*n
for idx,card in enumerate(cards):
  for idx2,card2 in enumerate(cards[idx+1:]):
    sum=card+card2
    for card3 in cards[idx+idx2+2:]:
      if sum+card3<=m and sum+card3>sum_list[idx]:
        sum_list[idx]=sum+card3

print(max(sum_list))
