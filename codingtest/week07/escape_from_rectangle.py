# 직사각형에서 탈출

#x, y, w, h=6, 2, 10, 3
x, y, w, h=map(int,input().split())

distance=[x, y, w-x, h-y]
print(min(distance))