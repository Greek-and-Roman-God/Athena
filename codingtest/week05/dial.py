#다이얼

def dial_time(num):
  dial_list=[
  ("A","B","C"),
  ("D","E","F"),
  ("G","H","I"),
  ("J","K","L"),
  ("M","N","O"),
  ("P","Q","R","S"),
  ("T","U","V"),
  ("W","X","Y","Z")
  ]

  for i,dial in enumerate(dial_list):
    if num in dial:
      return 3+i

word=input()
sum=0
for c in word:
  sum+=dial_time(c)
print(sum)