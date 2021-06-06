# 블록 이동하기

# 전형적인 BFS문제 유형
# 문제에서 로봇이 존재할 수 있는 각 위치(각 칸)를 노드로 보고, 인접한 위치와 비용이 1인 간선으로 연결되어 있다고 볼 수 있음
# 간선의 비용이 모두 1로 동일하기 때문에 BFS를 이용하여 최적의 해를 구할 수 있다.
# (1,1) 위치에 존재하는 로봇을 (N,N) 위치로 옮기는 최단 거리를 계산하는 문제
# 파이썬에서 집합 자료형은 {(1,2) (1,1)}과 {(1,1) (1,2)}를 같은 집합 객체로 처리한다.

# 이동 : 단순히 상,하,좌,우로 이동하는 경우를 계산하면 된다
# 회전 : 로봇이 가로로 놓여있는 경우, 세로로 놓여있는 경우로 나누어야 한다.
# 1. 가로 : 아래쪽으로 회전하는 경우에는 아래쪽에 벽이 없어야 하고, 위쪽으로 회전하는 경우에는 위쪽에 벽이 없어야 한다.
# 2. 세로 : 오른쪽으로 회전하는 경우에는 오른쪽에 벽이 없어야 하고, 왼쪽으로 회전하는 경우에는 왼쪽에 벽이 없어야 한다.

# 코드를 간단하게 작성하기 위해 초기에 주어진 맵의 외곽에 벽을 두른다.


from collections import deque

# 특정한 위치에서 이동 가능한 다음 위치를 반환하는 함수
def get_next_post(pos, board):
    next_pos=[] #반환 결과 (이동 가능한 위치들)
    pos=list(pos) # 현재 위치 정보를 리스트로 변환 (집합->리스트)
    pos1_x, pos1_y, pos2_x, pos2_y=pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우로 이동하는 경우에 대해서 처리
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y=pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
            next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
    # 로봇이 가로로 놓여있는 경우
    if pos1_x == pos2_x:
        for i in [-1,1]: # 위쪽, 아래쪽 으로 회전
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x+i,pos2_y)})
    # 로봇이 세로로 놓여있는 경우
    elif pos1_y==pos2_y:
        for i in [-1,1]: # 왼쪽, 오른쪽 으로 회전
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x,pos2_y+i)})
    return next_pos

def solution(board):
    #맵의 외곽에 벽을 두는 형태로 맵 변형
    n=len(board)
    now_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            now_board[i+1][j+1]=board[i][j]
    
    q=deque()
    visited=[]
    pos={(1,1),(1,2)} # 시작 위치 설정
    q.append((pos,0))
    visited.append(pos) # 방문 처리

    while q:
        pos, cost=q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_post(pos, now_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited(next_pos)
    return 0