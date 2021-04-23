#상근이 동생 상수

def reverse_num(num):
  reverse=list(str(num))
  reverse.reverse()
  reverse=("".join(reverse))
  return reverse

a, b=map(int, input().split())

a=reverse_num(a)
b=reverse_num(b)
print(max(a,b))