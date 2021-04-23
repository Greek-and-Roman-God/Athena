#크로아티아 알파벳

word="ljes=njak"
#word=input()
cro=["c=","c-","d-","lj","nj","s=","z="]

i=0
cnt=0
while i<len(word):
  if word[i:i+2] in cro:
    i+=2
  elif word[i:i+3] == "dz=":
    i+=3
  else:
    i+=1
  cnt+=1
print(cnt)