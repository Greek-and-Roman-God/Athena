# 문자열 뒤집기

s=list(map(int, list(input())))

cnt_0=0
cnt_1=0

for i in range(len(s)-1):
    if s[i]==0 and s[i+1]==1:
        cnt_0+=1
    if s[i]==1 and s[i+1]==0:
        cnt_1+=1
if s[-1]==0:
    cnt_0+=1
else:
    cnt_1+=1

print(min(cnt_0, cnt_1))