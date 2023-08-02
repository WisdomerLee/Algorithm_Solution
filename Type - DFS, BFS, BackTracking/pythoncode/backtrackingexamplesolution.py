#boj.kr/11724 : ���� ����� ����

#����: ���� ���� �׷����� �־����� �� ���� ���(connected component)�� ������ ���ϴ� ���α׷�

#�Է�: ù° �ٿ� ������ ���� N�� ������ ���� M�� �־��� (1<=N<=1000, 0<=M<=N(N-1)/2) ��° �ٺ��� M���� �ٿ� ������ �� ���� u�� v�� �־��� (1<=u,v<=N, u!=v) ���� ������ �� ����

#���: ù° �ٿ� ���� ����� ������ ���

#���� ���� ��� �� �ϳ� : üũ �迭�� �ϳ� �����...
#�ݺ����� ���鼭 false�� ���̸� ������...
#DFS�� ����

import sys

#�Է��� �ſ� ���� �ְ� �ȴٸ� ���� �Է��� Ȱ���� ��!!
input = sys.stdin.readline


#sys.setrecursionlimit(10**6)
#�⺻ : recursion : 1000�� �̻� �Ѿ�� ������ ���

#�Է��� �޾Ƽ� N�� M�� ���ڸ� �ް�
N, M = map(int, input().split())
#N���� 0���� ������ ����Ʈ �����
adj = [[0]*N for _ in range(N)]

for _ in range(M):
    #�Է��� �޾�
    a, b = map(lambda x: x-1, map(int, input().split()))
    #�ش� �Է¹��� ���� �ֿ� ���� ���� ����Ǿ��ٴ� ���� 1�� �ְ�
    adj[a][b] = adj[b][a]=1

#�׷��� ���� �Է�
ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            #����ȭ�� ���� ���� check�Ǿ����� ó���ϰ�
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans +=1
        chk[i] =True
        dfs(i)

print(ans)

#���� : NxM ũ���� �迭�� ǥ���Ǵ� �̷ΰ� ����
#1�� �̵��� �� �ִ� ��, 0�� �̵��� �� ���� ��
#�̷��� �̷ΰ� �־����� �� (1,1)���� ����Ͽ� (N,M�� ��ġ�� �̵��� �� ������ �ϴ� �ּ� ĭ�� ���� ���ϴ� ���α׷��� �ۼ��� ��, �� ĭ���� �ٸ� ĭ���� �̵��� �� ���� ������ ĭ���θ� �̵��� �� ����)
#ĭ�� �� �� ����, ���� ��ġ�� ������ ��

#�Է�: ù° �ٿ� �� ���� N, M(2<=N,M<=100)�� �־���, N���� �ٿ��� M���� ������ �̷ΰ� �־���. ������ ������ �پ �Է����� �־���

#���: 

#�������� �� ã��
#BFS�� �ִ� �Ÿ� �˰��� �߿� �ϳ��̹Ƿ�... BFS�� �� ��

from collections import deque

dy=(0, 1, 0, -1)
dx=(1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y,x):
    return 0 <= y< N and 0 <= x <M


def bfs():
    chk= [[False]*M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0, 1)) #y, x, �̵��� ĭ ��
    while dq:
        y,x,d = dq.popleft()

        if y==N-1 and x==M-1:
            return d

        nd = d+1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx]
                dq.append((ny, nx, nd))

bfs()

#�׷���: node, edge�� ������
#���⼺�� ��ȯ���� �ְų� ���� �� ����
#�� �� ���� ��� Tree��� �θ�
#�ſ� ���� �׷���, Ʈ�� ������ �˰����� ������
#�׷����� �ڵ�� ������ ��
#-�������: edge�� ���� �׷����� ��, edgeŽ���� ����
#-��������Ʈ: edge�� ���� �׷����� ��, �޸𸮸� ���� ��
#DFS, BFS, ��Ʈ��ŷ : ���� Ž�� �˰���
#�ִ� �Ÿ��� ���� �� BFS�� ��
#DFS�� ���(Ȥ�� stack), BFS�� queue�� ����
#����ġ�Ⱑ ������ backtracking
