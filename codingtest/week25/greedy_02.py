# 곱하기 혹은 더하기

s=list(map(int, list(input())))

ans=0
for i in range(len(s)):
    if 0 in (s[i], ans):
        ans+=s[i]
        continue
    ans*=s[i]

print(ans)