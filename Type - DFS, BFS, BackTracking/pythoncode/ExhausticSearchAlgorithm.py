#완전 탐색 알고리즘! : 모든 경우의 수를 다 확인하기 때문에 어떤 상황에서든 값을 얻어냄(가능, 불가능한 것들도 알아냄)


#시간 제한 : 1초, 입력 2<=N <= 1,000,000
#N개의 숫자가 주어졌을 때 짝의 합이 최대일 경우??
#정렬을 시켜 두 수를 더 하게 하기
#기본 정렬: O(NlogN)이 됨

#순열 : permutation
#모든 경우의 수를 순서대로 살펴볼 때 용이

from itertools import permutations

v = [0, 1,2,3]
#permutations : 첫번째 인자: 배열, 두번째 인자 뽑을 갯수 : 이것은 순서와 관련 있음 
for i in permutations(v, 4):
    print(i)

#조합 combinations
from itertools import combinations

v = [0,1,2,3]
#permutations : 첫번째 인자: 배열, 두번째 인자 뽑을 갯수 : 순서가 달라도 같은 조합으로 취급!
for i in combinations(v, 2):
    print(i)

#boj.kr/2309
#문제 : 백설공주가 일과를 마치고 돌아온 난쟁이가 일곱이 아닌 아홉이었다
#일곱 난쟁이의 키 합이 100이었는데 아홉 난쟁이의 키가 주어졌을 때 일곱난쟁이를 찾는 프로그램을 작성하기

#입력: 아홉줄에 걸쳐 난쟁이들의 키가 주어짐 : 각 키는 100을 넘지 않는 자연수, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여럿일 경우 그 중에 아무것이나 출력할 것

#출력: 일곱 난쟁이의 키를 오름차순으로 출력


from itertools import combinations

#입력을 9번에 걸쳐 받음
heights = [int(input()) for _ in range(9)]

for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
        break

#모든 경우의 수를 다 살펴보아도 시간 초과가 나지 않을 경우 완전 탐색 알고리즘의 형태로 시도해 볼 것!
#시간 초과가 될 경우엔.. 보다 효율적인 알고리즘을 찾을 것!
