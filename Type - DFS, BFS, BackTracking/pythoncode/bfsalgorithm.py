from collections import deque

adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
#... : 

#dfs와 tree의 구조는 같으나 연결이 되는 부분이 다르게 됨...

def bfs(now):
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs(0)

#길찾기 문제

dy = (0,1,0,-1)
dx = (1,0,-1,0)
chk = [[False]*100 for _ in range(100)]
N = int(input())

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y,x = q.popleft()
        #방문한 곳은 더 이상 방문하지 않도록 방문한 곳을 체크하고
        chk[y][x] = True
        #방향 네군데를 따져서
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))

