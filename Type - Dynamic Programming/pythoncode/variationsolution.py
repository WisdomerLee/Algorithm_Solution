#다채로운 문제들을 확인하고 솔루션을 작성하며 확인하기

#체스판 다시 칠하기
#시간 2초, 메모리 128MB
#문제 : MN개의 단위 정사각형으로 나뉜 MxN크기의 보드가 있다. 어느 정사각형은 검은색, 나머지는 흰 색으로 칠해져 있다. 이 보드를 잘라서 8x8크기의 체스판을 만들려고 함
#체스판은 검은, 흰 색이 번갈아 채색되어야 함. 체스판을 칠하는 경우는 단 두가지 뿐, 하나는 맨 왼쪽 위 칸이 흰색이거나 검은색인 경우
#보드가 체스판처럼 칠해져 있다는 보장이 없어 8x8 크기의 체스판으로 잘라낸 뒤, 몇 개의 정사각형을 다시 색칠하려 함, 다시 칠해야 하는 정사각형의 최소 갯수를 구하는 프로그램

#입력 : 첫째 줄에 N, M이 주어짐, N,M은 8과 50 사이의 자연수, 둘째줄부터 N개의 줄에는 보드의 각 행의 상태가 주어짐, B:검은색, W: 흰색
#

#먼저 완전탐색 알고리즘부터 고민해보기...
#시간 제한과 메모리 제한에 걸리는지 파악하고 걸리지 않으면 그 알고리즘대로 진행할 것, 그렇지 않으면... 다른 알고리즘을 생각할 것?
#위의 경우 숫자가 크지 않아 연산숫자가 1억이 넘지 않아 제한시간 2초 이내에 충분히 풀 수 있는 것

N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2:
                if board[y+i][x+j] == bw:
                    cnt+=1
            else:
                if board[y+i][x+j] != bw:
                    cnt+=1
    ans = min(ans, cnt)

for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(ans)

#누적합을 이용해서 구하는 방법도 있다고 함

#boj.kr/2841
#시간 1초, 메모리 256MB

#문제: 

#boj.kr/4796
#시간 1초, 메모리 128MB
#캠핑장은 연속하는 20일 중 10일 동안만 쓸 수 있음, 28일 중에 캠핑장을 쓸 수 있는 기간은?
#조금더 일반화 하여 연속하는 P일 중 L기간만 쓸 수 있음, V일짜리 휴가 중 최대로 쓸 수 있는 캠핑장 날짜는??

#입력: L,P,V를 순차로 입력 받음
#출력: 최대 날짜

#P구간마다 L의 기간을 쓸 수 있으므로 전체 V의 일정을 P로 나누어 해당되는 P의 구간마다 L을 이용하고 가장 마지막의 P의 구간은.. P로 나눈 몫*L + min(L, V%P)
tc = 1
while True:
    L, P, V = map(int, input().split())
    if L ==0:
        break;
    print(f'Case {tc}: {V//P*L + min(L, V%P)}')
    tc+=1


#boj.kr/15686
#문제 : 

#입력 : 

#출력 : 

from collections import deque
from itertools import combinations, combinations_with_replacement

N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
    #아래와 같이 처리하면 index와 데이터를 한 번에 처리할 수 있음 enumerate
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))
#최소 값을 구하는 문제여서 임의의 아주 커다란 (절대 나올 수 없는 값을 넣어두기)
ans = 2 * N * len(houses)

def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for combi in combinations(chickens, M):
    tot = 0 
    for house in houses:
        tot += min(get_dist(house, chicken) for chicken in combi)
            
    ans = min(ans, tot)

print(ans)


#boj.kr/1389

N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

for row in adj:
    print(row)

kevin = []
ans = (-1, 9999999999999)


def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d

        nd = d+1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))


def get_kevin(start):
    tot = 0

    for i in range(N):
        if i != start:
            tot += bfs(start, i)

    return tot


for i in range(N):
    kevin.append(get_kevin(i))


for i, v in enumerate(kevin):
    if ans[1] > v:
        ans = (i, v)

print(kevin[0])

#boj.kr/1915

n, m = map(int, input().split())
arr =[input() for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

for i in range(1, n):
    if arr[i][0] == '1':
        dp[i][0]= 1

    for j in range(1, m):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+1)

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans **2)



#dp(i, j) :i, j칸을 우하단으로 하는 정사각형 최대 크기

#boj.kr/17136

#greedy 탐욕 알고리즘
#backtracking으로

board = [list(map(int, input().split())) for _ in range(10)]

ans = 25

paper = [0] * 6

def is_possible(y, x, sz):
    if paper[sz] == 5:
        return False

    if y+sz >10 or x+sz >10:
        return False
    for i in range(sz):
        for j in range(sz):
            if board[y+1][x+j] == 0:
                return False
    return True

def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y+i][x+j]=v

    if v:
        paper[sz]-=1
    else:
        paper[sz]+=1

def backtracking(y,x):
    global ans
    if y==10:
        ans = min(ans, sum(paper))
        return
    if x==10:
        backtracking(y+1, 0)
        return

    if board[y][x] == 0:
        backtracking(y, x+1)
        return

    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x+1)
            mark(y, x, sz, 1) #원상복구



backtracking(0,0)

print(-1 if ans ==25 else ans)


#boj.kr/1213
from collections import Counter


c = dict()
s = input()
for ch in s:
    if ch in c:
        c[ch] +=1
    else:
        c[ch] =1

if sum(i %2 for i in c.values())>1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for k, v in sorted(c.items()):
        half += k * (v//2)

    ans = half
    for k, v in c.items():
        if v%2:
            ans += k
            break

    ans += ''.join(reversed(half))
    print(ans)

#Counter를 쓰는 경우 : Counter는 dictionary와 비슷한데 몇개가 쓰였는지를 보여줌....
c = Counter(input())
if sum(i %2 for i in c.values())>1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for k, v in sorted(c.items()):
        half += k * (v//2)

    ans = half
    for k, v in c.items():
        if v%2:
            ans += k
            break

    ans += ''.join(reversed(half))
    print(ans)