#��ä�ο� �������� Ȯ���ϰ� �ַ���� �ۼ��ϸ� Ȯ���ϱ�

#ü���� �ٽ� ĥ�ϱ�
#�ð� 2��, �޸� 128MB
#���� : MN���� ���� ���簢������ ���� MxNũ���� ���尡 �ִ�. ��� ���簢���� ������, �������� �� ������ ĥ���� �ִ�. �� ���带 �߶� 8x8ũ���� ü������ ������� ��
#ü������ ����, �� ���� ������ ä���Ǿ�� ��. ü������ ĥ�ϴ� ���� �� �ΰ��� ��, �ϳ��� �� ���� �� ĭ�� ����̰ų� �������� ���
#���尡 ü����ó�� ĥ���� �ִٴ� ������ ���� 8x8 ũ���� ü�������� �߶� ��, �� ���� ���簢���� �ٽ� ��ĥ�Ϸ� ��, �ٽ� ĥ�ؾ� �ϴ� ���簢���� �ּ� ������ ���ϴ� ���α׷�

#�Է� : ù° �ٿ� N, M�� �־���, N,M�� 8�� 50 ������ �ڿ���, ��°�ٺ��� N���� �ٿ��� ������ �� ���� ���°� �־���, B:������, W: ���
#

#���� ����Ž�� �˰������ ����غ���...
#�ð� ���Ѱ� �޸� ���ѿ� �ɸ����� �ľ��ϰ� �ɸ��� ������ �� �˰����� ������ ��, �׷��� ������... �ٸ� �˰����� ������ ��?
#���� ��� ���ڰ� ũ�� �ʾ� ������ڰ� 1���� ���� �ʾ� ���ѽð� 2�� �̳��� ����� Ǯ �� �ִ� ��

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

#�������� �̿��ؼ� ���ϴ� ����� �ִٰ� ��

#boj.kr/2841
#�ð� 1��, �޸� 256MB

#����: 

#boj.kr/4796
#�ð� 1��, �޸� 128MB
#ķ������ �����ϴ� 20�� �� 10�� ���ȸ� �� �� ����, 28�� �߿� ķ������ �� �� �ִ� �Ⱓ��?
#���ݴ� �Ϲ�ȭ �Ͽ� �����ϴ� P�� �� L�Ⱓ�� �� �� ����, V��¥�� �ް� �� �ִ�� �� �� �ִ� ķ���� ��¥��??

#�Է�: L,P,V�� ������ �Է� ����
#���: �ִ� ��¥

#P�������� L�� �Ⱓ�� �� �� �����Ƿ� ��ü V�� ������ P�� ������ �ش�Ǵ� P�� �������� L�� �̿��ϰ� ���� �������� P�� ������.. P�� ���� ��*L + min(L, V%P)
tc = 1
while True:
    L, P, V = map(int, input().split())
    if L ==0:
        break;
    print(f'Case {tc}: {V//P*L + min(L, V%P)}')
    tc+=1


#boj.kr/15686
#���� : 

#�Է� : 

#��� : 

from collections import deque
from itertools import combinations, combinations_with_replacement

N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
    #�Ʒ��� ���� ó���ϸ� index�� �����͸� �� ���� ó���� �� ���� enumerate
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))
#�ּ� ���� ���ϴ� �������� ������ ���� Ŀ�ٶ� (���� ���� �� ���� ���� �־�α�)
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



#dp(i, j) :i, jĭ�� ���ϴ����� �ϴ� ���簢�� �ִ� ũ��

#boj.kr/17136

#greedy Ž�� �˰���
#backtracking����

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
            mark(y, x, sz, 1) #���󺹱�



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

#Counter�� ���� ��� : Counter�� dictionary�� ����ѵ� ��� ���������� ������....
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