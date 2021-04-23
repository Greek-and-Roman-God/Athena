# 달팽이는 올라가고 싶다

a, b, v=map(int, input().split())

# cnt=1
# while v>a:
#   cnt+=1
#   v-=(a-b)
# print(cnt)


cnt=(v-a)//(a-b)
remain=(v-a)%(a-b)
if remain>0:
  cnt+=1

print(cnt+1)