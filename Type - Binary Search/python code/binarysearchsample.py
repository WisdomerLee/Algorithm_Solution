#C++에서는 lower/upper_bound가 있음

from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)

three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)
print(f'number of 3 : {three}')
print(f'number of 4 : {four}')
print(f'number of 6 : {six}')

#bisect_right: 탐색된 값 중 가장 오른쪽(뒤의) index
#bisect_left : 탐색된 값 중 가장 왼쪽(앞의) index


#시간제한 1초, 메모리제한 128MB
#문제 : 국가의 역할 중 하나는 지방의 예산 요청을 심사하여 국가의 예산을 분배하는 것, 국가 예산의 총액은 미리 정해져 있어 모든 예산 요청을 배정해주기 어려울 수도 있음
#가능한한 최대의 총 예산을 다음과 같은 방법으로 배정
# 모든 요정이 배정될 수 있는 경우는 요청한 금액을 그대로 배정
# 모든 요청이 배정될 수 없는 경우는 특정한 정수 상한액을 계산하여 그 이상인 예산 요청에는 모두 상한액을 배정, 상한액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정
#국가 예산이 485고 4개의 지방의 예산 요청이 120, 110, 140, 150일 때 상한액을 127로 잡으면 해당 요청에 대해 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 됨
#여러 지방의 예산 요청과 국가 예산의 총액이 주어졌을 때 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하기

#입력 : 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어짐, N은 3이상 1만 이하, 각 지방의 예산 요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어짐 이 값들은 1과 십만 사이
#그 다음 줄에는 총 예산을 나타내는 정수 M이 주어짐. M은 N이상 1백억 이하
#출력 : 배정된 예산들 중 최댓값인 정수를 출력하기!

N = int(input())
req = list(map(int, input().split()))
M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi)//2
ans = 0

def if_possible(mid):
    #req를 반복하면서 mid와 r중에 최소 값을 모두 더해 최종 예산을 넘지 않는지 확인 : 조건을 참, 거짓으로 만들수 있는 상태를 만들고 이 상태를 이진탐색으로 찾아가는 방식
    return sum(min(r, mid) for r in req) <= M



while lo<=hi:
    if if_possible(mid):
        lo = mid+1
        ans = mid
    else:
        hi = mid -1

    mid = (lo+hi) // 2

print(ans)


#boj.kr/

#문제: 숫자 카드는 정수 하나가 적힌 카드, 상근이는 숫자 카드 N개를 갖고 있음. 정수 M개가 주어졌을 때 이 숫자가 적힌 숫자 카드를 상근이가 갖고 있는지 아닌지를 구하는 프로그램

#입력: 첫째 줄에 상근이가 갖고 있는 숫자 카드의 갯수N(1<=N<=500,000)이 주어지고 둘째 줄에는 숫자 카드가 적혀있는 정수가 주어짐 숫자 카드에 적힌 숫자는 -10,000,000<=L <= 10,000,000, 숫자 카드의 숫자는 모두 다름
#셋째 줄에는 M(1<=M<=500,000) , 넷째 줄에는 상근이가 갖고 있는 숫자 카드인지 아닌지 구해야 할 M개의 정수가 주어지고 이 숫자는 공백으로 구분, 이 숫자도 L과 같은 범위

from bisect import bisect_left, bisect_right

#N과 M은 C++인 경우에 필요하기 때문에 문제에 포함됨...
N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    #카드가 존재한다면...? r-l이 0보다 큰 숫자로 나옴
    ans.append(1 if r-l else 0)

print(*ans)

#Binary Search : 