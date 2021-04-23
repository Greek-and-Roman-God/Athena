#알파벳 찾기

s=input()

alphabet=[-1]*26

for i,c in enumerate(s):
  if alphabet[ord(c)-97]==-1:
    alphabet[ord(c)-97]=i

for a in alphabet:
  print(a,end=" ")
