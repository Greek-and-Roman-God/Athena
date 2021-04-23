#그룹 단어 체커

n=4
words=["aba","baa","abcabc","a"]
# n=int(input())
# words=[]
# for _ in range(n):
#   words.append(input())

cnt=0
for word in words:
  temp=word[0]
  alphabet=[word[0]]
  for w in word[1:]:
    if temp!=w:
      if w in alphabet:
        break
      temp=w
      alphabet.append(w)
  else:
    cnt+=1

print(cnt)