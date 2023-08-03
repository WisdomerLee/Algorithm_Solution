#boj.kr/2748
#�Ǻ���ġ ����

#�Ǻ���ġ ���ڸ� �̿��ϱ�!

#Top-down ���
#memoization �����ϱ�
cache = [-1] * 91
cache[0] = 0
cache[1] =1

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]
    #if n==0:
    #    return 0
    #elif n==1:
    #    return 1
    #return f(n-1) + f(n-2)

print(f(int(input())))

#memoization�� ������ ����Լ��� ȣ��Ǵ� ���ڰ� �İ������� ����....��

#Bottom-up ���
#Tabulation ���� 
N = int(input())
cache = [-1]*91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
    cache[i] = cache[i-1]+cache[i-2]

print(cache[N])
