# 감시 피하기

from itertools import combinations

n=int(input())
board=[]
teachers=[]
spaces=[]

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j]=='T': # 선생님 위치 저장
            teachers.append((i,j))
        if board[i][j]=='X': # 공간 위치 저장
            spaces.append((i,j))

# 선생님의 위치에서 학생을 발견할 수 있는지 판별하는 메서드
def watch(x,y,direction):
    if direction==0: # 왼쪽
        while y>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y-=1
    if direction==1: # 오른쪽
        while y<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y+=1
    if direction==2: # 위쪽
        while x>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x-=1
    if direction==3: # 아래쪽
        while x<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x+=1
    return False

# 장애물 설치 이후 학생이 감지되는지 검사
def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
        return False

find=False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y]='0'
    if not process():
        find=True
        break
    for x,y in data:
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')