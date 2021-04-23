#단어 공부

word=input()
word=word.upper()
alpha_dict={}
for c in word:
  if c in alpha_dict:
    alpha_dict[c]=alpha_dict[c]+1
  else:
    alpha_dict[c]=1

value_list=list(alpha_dict.values())
out="?"
if value_list.count(max(value_list))==1:
  for k,v in alpha_dict.items():
    if v==max(value_list):
      out=k
      break
print(out)