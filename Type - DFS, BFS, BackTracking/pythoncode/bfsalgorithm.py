from collections import deque

adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
#... : 

#dfs�� tree�� ������ ������ ������ �Ǵ� �κ��� �ٸ��� ��...

def bfs(now):
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs(0)

#��ã�� ����

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
        #�湮�� ���� �� �̻� �湮���� �ʵ��� �湮�� ���� üũ�ϰ�
        chk[y][x] = True
        #���� �ױ����� ������
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))

