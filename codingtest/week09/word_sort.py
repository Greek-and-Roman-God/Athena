# 단어 정렬

# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

n=int(input())
words=[]
for _ in range(n):
  words.append(input())

words=sorted(list(set(words)))
words=sorted(words, key=lambda x: len(x))

for w in words:
  print(w)