#boj.kr/11051
#���װ��

#���� �ڿ��� N�� ���� K�� �־����� �� ���� ��� (N K)�� 10007�� ���� �������� ���ϴ� ���α׷�
#�Է� : ù° �ٿ� N, K�� �־���(1<=N <=1000, 0<=K <=N)

#top-down��� 
import sys

MOD = 10007

sys.setrecursionlimit(10**7)
#�⺻���� �ݺ��� Ƚ���� õ�� �̸��̳� �� �Ѱ踦 �÷��ֱ� > ���̽��� ���� ����̱� ������ �ش� ������ ���� �ɷ��ִ� ��

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

#bottom-up���
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


#���� 1��, �޸� 256MB
#���� : 2xnũ���� ���簢���� 1x2, 2x1Ÿ�Ϸ� ä��� ����� ���� ���ϴ� ���α׷�

#�Է�: ù° �ٿ� n�� �־���(1<=n<=1000)
#���: ���簢���� ä��� ����� ���� 10007�� ���� �������� ���

#����� �� ���踦 ���캸�� >>f(1) =1, f(2)=2, f(3) =3, f(4)= 5, f(5)= 8,...������ ��Ÿ���µ�
#f(n) = f(n-1)+f(n-2)�� ���谡 �������� �� �� ����


MOD = 10_007

dp = [0] *1001
dp[1] =1
dp[2] =2

n = int(input())

for i in range(3, 1001):
    dp[i] = (dp[i-1]+dp[i-2])%MOD

print(dp[n])


#boj.kr/10844
#����: 1��, �޸� 256MB
#���� 45656 : ������ ��� �ڸ��� ���̰� 1 > ��ܼ���� ��
#N�� �־��� �� ���̰� N�� ��ܼ��� �� �� ������ Ȯ���ϱ�! 0���� �����ϴ� ���� ��ܼ��� �ƴ�

#�Է�: ù° �ٿ� N�� �־���, N�� 1�� 100������ �ڿ���
#���: 1,000,000,000���� ���� �������� ����ϱ�

#��ܼ��� �������� ���踦 ã�Ƴ��� ���� ���� Ǯ���� ��¥

MOD = 1_000_000_000

#cache[n][d] : ���̰� n, ������ ���ڰ� d�� ��ܼ��� ����
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