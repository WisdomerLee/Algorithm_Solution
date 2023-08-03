#boj.kr/2748
#피보나치 숫자

#피보나치 숫자를 이용하기!

#Top-down 방식
#memoization 적용하기
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

#memoization이 없으면 재귀함수로 호출되는 숫자가 파격적으로 증가....함

#Bottom-up 방식
#Tabulation 적용 
N = int(input())
cache = [-1]*91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
    cache[i] = cache[i-1]+cache[i-2]

print(cache[N])
