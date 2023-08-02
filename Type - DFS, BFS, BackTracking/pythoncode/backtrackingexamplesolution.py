#boj.kr/11724 : 연결 요소의 갯수

#문제: 방향 없는 그래프가 주어졌을 때 연결 요소(connected component)의 갯수를 구하는 프로그램

#입력: 첫째 줄에 정점의 갯수 N과 간선의 갯수 M이 주어짐 (1<=N<=1000, 0<=M<=N(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어짐 (1<=u,v<=N, u!=v) 같은 간선은 한 번만

#출력: 첫째 줄에 연결 요소의 갯수를 출력

#문제 접근 방식 중 하나 : 체크 배열을 하나 만들고...
#반복문을 보면서 false인 아이를 만나면...
#DFS를 돌림

import sys

#입력이 매우 자주 있게 된다면 빠른 입력을 활용할 것!!
input = sys.stdin.readline


#sys.setrecursionlimit(10**6)
#기본 : recursion : 1000번 이상 넘어가면 에러를 띄움

#입력을 받아서 N과 M의 숫자를 받고
N, M = map(int, input().split())
#N개의 0으로 구성된 리스트 만들기
adj = [[0]*N for _ in range(N)]

for _ in range(M):
    #입력을 받아
    a, b = map(lambda x: x-1, map(int, input().split()))
    #해당 입력받은 숫자 쌍에 대해 서로 연결되었다는 정보 1을 주고
    adj[a][b] = adj[b][a]=1

#그래프 정보 입력
ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            #최적화를 위해 먼저 check되었음을 처리하고
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans +=1
        chk[i] =True
        dfs(i)

print(ans)

#문제 : NxM 크기의 배열로 표현되는 미로가 있음
#1은 이동할 수 있는 곳, 0은 이동할 수 없는 곳
#이러한 미로가 주어졌을 때 (1,1)에서 출발하여 (N,M의 위치로 이동할 때 지나야 하는 최소 칸의 수를 구하는 프로그램을 작성할 것, 한 칸에서 다른 칸으로 이동할 때 서로 인접한 칸으로만 이동할 수 있음)
#칸을 셀 땐 시작, 도착 위치도 포함할 것

#입력: 첫째 줄에 두 정수 N, M(2<=N,M<=100)이 주어짐, N개의 줄에는 M개의 정수로 미로가 주어짐. 각각의 수들은 붙어서 입력으로 주어짐

#출력: 

#전형적인 길 찾기
#BFS는 최단 거리 알고리즘 중에 하나이므로... BFS를 쓸 것

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
    dq.append((0, 0, 1)) #y, x, 이동한 칸 수
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

#그래프: node, edge로 구성됨
#방향성과 순환성이 있거나 없을 수 있음
#둘 다 없는 경우 Tree라고 부름
#매우 많은 그래프, 트리 종류와 알고리즘이 존재함
#그래프를 코드로 구현할 때
#-인접행렬: edge가 많은 그래프일 때, edge탐색이 빠름
#-인접리스트: edge가 적은 그래프일 때, 메모리를 적게 씀
#DFS, BFS, 백트래킹 : 완전 탐색 알고리즘
#최단 거리를 구할 땐 BFS를 씀
#DFS는 재귀(혹은 stack), BFS는 queue로 구현
#가지치기가 있으면 backtracking
