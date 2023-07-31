
#알고리즘 문제 출처: 백준
#boj.kr/9012
#알고리즘 문제
#괄호 문자열(Parenthesis String, PS)는 두 개의 괄호 기호인 '(',')'만으로 구성된 문자열
#괄호의 모양이 바르게 구성된 문자열이 올바른 괄호 문자열(Valid PS, VPS)라 함 기본 VPS :"()"
#만약 x가 VPS면 "(x)"도 VPS
#두 VPS x,y를 접합(concantenation)시킨 새 문자열 xy도 VPS
#입력으로 주어진 괄호 문자열이 VPS인지 아닌지 판단하여 그 결과를 YES와 NO로 나타내기

#입력데이터는 표준 입력을 쓸 것, 입력은 T개의 테스트 데이터로 주어짐, 입력의 첫번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어짐
#각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한줄에 주어짐, 하나의 괄호 문자열의 길이 2~50

#괄호의 문자 형태를 파악하여 열린 괄호로 시작하여 닫힌 괄호를 만나고 그 갯수가 같은지를 판별해야 함

#stack을 이용하여 풀이

for _ in range(int(input())):
    stk = []
    isVPS = True
    for char in input():
        if char == '(':
            stk.append(char)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break
    
    if stk:
        isVPS = False

    print('YES' if isVPS else 'NO')

#boj.kr/2164

#N장의 카드가 있음, 각 카드는 차례대로 1부터 N까지 번호가 붙어있고 1번 카드가 제일 위, N번 카드가 제일 아래인 상태
#다음의 동작을 카드가 한장 남을 때까지 반복 제일 위의 카드를 바닥에 버리고 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
#N=4인경우 카드는 1234로 놓여있고 1을 버려 234가 남고 2를 밑으로 옮겨 342가 됨 3을 버려 42가 되고 4를 밑으로 옮겨 24가 됨, 2를 버리고 나면 남는 카드는 4가 됨
#N이 주어졌을 때 제일 마지막에 남는 카드를 구하는 프로그램을 구하기 제한시간 2초, 메모리 제한 128MB!

#입력: 정수 N(1<=N<=500,000)이 주어짐
#출력: 남는 카드 번호를 출력할 것

#가장 위에 있는 것을 빼고 그 다음 가장 위에 있는 것을 아래로 넣어야 하므로 삽입, 삭제가 반복!
#Queue를 쓰기! : 배열의 경우 삽입, 삭제시 O(N)인데 그것이 반복되므로 O(N^2)이 됨. : 50만을 넣으면 배열로 구현하면 시간이 몇십초 이상 소요됨.......

from collections import deque


N = int(input())
dq = deque(range(1, N+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())

#boj.kr/11286

#시간 제한 1초, 메모리 제한 256MB

#절댓값 힙은 다음과 같은 연산을 지원하는 자료구조
#배열에 정수 x를 넣음
#배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거, 절댓값이 가장 작은 값이 여럿일 때는 가장 작은 수를 출력하고 그 값을 배열에서 제거
#프로그램은 빈 배열부터 시작

#첫째 줄에 연산의 갯수 N(1<=N<=100,000)이 주어짐, 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어짐, x가 0이 아니라면 배열에 x라는 값을 넣는 연산이고 x가 0이면
#배열에서 절댓값이 가장 작은 값을 출력하고 해당 값을 배열에서 제거, 입력되는 정수는 -2^31보다 크고 2^31보다 작음
#

import heapq as hq
import sys
#빠른 입력이 필요함....
input = sys.stdin.readline

pq=[]
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0) #이 한줄이 아래와 같은 효과를 냄!
        #if pq:
        #    print(hq.heappop(pq))
        #else:
        #    print(0)


#boj.kr/1302

#시간제한 2초, 메모리제한 128MB

#문제 : 김형택은 탑문고의 직원, 계산대에서 계산도 함, 근무가 끝나면 오늘 판매한 책의 제목을 보고 가장 많이 팔린 책의 제목을 칠판에 써두는 일도 같이 함
#오늘 하룻동안 팔린 책의 제목이 입력으로 들어왔을 때 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성

#입력: 첫째 줄에 오늘 하루 동안 팔린 책의 갯수 N이 주어짐, 이 값은 1000보다 작거나 같은 숫자, 둘째부터 N개의 줄에 책의 제목이 입력으로 들어옴, 책 제목의 길이는 50보다 작거나 같고 알파벳 소문자로만 구성

#출력: 첫째 줄에 가장 많이 팔린 책의 제목을 출력, 만약 가장 많이 팔린 책이 여럿일 경우 사전 순서대로 가장 앞의 제목을 출력할 것

d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
candi = []
for k, v in d.items():
    if v ==m:
        candi.append(k)

print(sorted(candi)[0])
