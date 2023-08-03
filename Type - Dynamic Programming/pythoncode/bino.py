#boj.kr/11051
#이항계수

#문제 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 10007로 나눈 나머지를 구하는 프로그램
#입력 : 첫째 줄에 N, K가 주어짐(1<=N <=1000, 0<=K <=N)

#top-down방식 
import sys

MOD = 10007

sys.setrecursionlimit(10**7)
#기본적인 반복의 횟수가 천번 미만이나 그 한계를 늘려주기 > 파이썬은 느린 언어이기 때문에 해당 제한이 낮게 걸려있는 편

N, K = map(int, input().split())

cache = [[0]*1001 for _ in range(1001)]


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]
    if k==0 or k==n:
        cache[n][k]=1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] %= MOD
    return cache[n][k]



print(bino(N, K))

#bottom-up방식
MOD = 10007



cache = [[0]*1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    cache[i][0]=cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1]+cache[i-1][j]
        cache[i][j] %= MOD
for i in range(7):
    print(cache[i])


print(cache[N][K])


#제한 1초, 메모리 256MB
#문제 : 2xn크기의 직사각형을 1x2, 2x1타일로 채우는 방법의 수를 구하는 프로그램

#입력: 첫째 줄에 n이 주어짐(1<=n<=1000)
#출력: 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력

#경우의 수 관계를 살펴보면 >>f(1) =1, f(2)=2, f(3) =3, f(4)= 5, f(5)= 8,...등으로 나타나는데
#f(n) = f(n-1)+f(n-2)의 관계가 성립함을 알 수 있음


MOD = 10_007

dp = [0] *1001
dp[1] =1
dp[2] =2

n = int(input())

for i in range(3, 1001):
    dp[i] = (dp[i-1]+dp[i-2])%MOD

print(dp[n])


#boj.kr/10844
#제한: 1초, 메모리 256MB
#문제 45656 : 인접한 모든 자리의 차이가 1 > 계단수라고 함
#N이 주어질 때 길이거 N인 계단수가 총 몇 개인지 확인하기! 0으로 시작하는 수는 계단수가 아님

#입력: 첫째 줄에 N이 주어짐, N은 1과 100사이의 자연수
#출력: 1,000,000,000으로 나눈 나머지를 출력하기

#계단수의 갯수들의 관계를 찾아내는 것이 문제 풀이의 알짜

MOD = 1_000_000_000

#cache[n][d] : 길이가 n, 마지막 숫자가 d인 계단수의 갯수
cache= [[0]*10 for _ in range(101)]

for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j>0:
            cache[i][j] += cache[i-1][j-1]
            cache[i][j] %=MOD
        if j<9:
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %=MOD


ans =0

for j in range(10):
    ans+= cache[N][j]
    ans %=MOD

print(ans)