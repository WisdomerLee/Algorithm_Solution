#C++������ lower/upper_bound�� ����

from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)

three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)
print(f'number of 3 : {three}')
print(f'number of 4 : {four}')
print(f'number of 6 : {six}')

#bisect_right: Ž���� �� �� ���� ������(����) index
#bisect_left : Ž���� �� �� ���� ����(����) index


#�ð����� 1��, �޸����� 128MB
#���� : ������ ���� �� �ϳ��� ������ ���� ��û�� �ɻ��Ͽ� ������ ������ �й��ϴ� ��, ���� ������ �Ѿ��� �̸� ������ �־� ��� ���� ��û�� �������ֱ� ����� ���� ����
#�������� �ִ��� �� ������ ������ ���� ������� ����
# ��� ������ ������ �� �ִ� ���� ��û�� �ݾ��� �״�� ����
# ��� ��û�� ������ �� ���� ���� Ư���� ���� ���Ѿ��� ����Ͽ� �� �̻��� ���� ��û���� ��� ���Ѿ��� ����, ���Ѿ� ������ ���� ��û�� ���ؼ��� ��û�� �ݾ��� �״�� ����
#���� ������ 485�� 4���� ������ ���� ��û�� 120, 110, 140, 150�� �� ���Ѿ��� 127�� ������ �ش� ��û�� ���� 120, 110, 127, 127�� �����ϰ� �� ���� 484�� ������ �ִ밡 ��
#���� ������ ���� ��û�� ���� ������ �Ѿ��� �־����� �� ���� ������ ��� �����ϵ��� ������ �����ϴ� ���α׷��� �ۼ��ϱ�

#�Է� : ù° �ٿ��� ������ ���� �ǹ��ϴ� ���� N�� �־���, N�� 3�̻� 1�� ����, �� ������ ���� ��û�� ǥ���ϴ� N���� ������ ��ĭ�� ���̿� �ΰ� �־��� �� ������ 1�� �ʸ� ����
#�� ���� �ٿ��� �� ������ ��Ÿ���� ���� M�� �־���. M�� N�̻� 1��� ����
#��� : ������ ����� �� �ִ��� ������ ����ϱ�!

N = int(input())
req = list(map(int, input().split()))
M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi)//2
ans = 0

def if_possible(mid):
    #req�� �ݺ��ϸ鼭 mid�� r�߿� �ּ� ���� ��� ���� ���� ������ ���� �ʴ��� Ȯ�� : ������ ��, �������� ����� �ִ� ���¸� ����� �� ���¸� ����Ž������ ã�ư��� ���
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

#����: ���� ī��� ���� �ϳ��� ���� ī��, ����̴� ���� ī�� N���� ���� ����. ���� M���� �־����� �� �� ���ڰ� ���� ���� ī�带 ����̰� ���� �ִ��� �ƴ����� ���ϴ� ���α׷�

#�Է�: ù° �ٿ� ����̰� ���� �ִ� ���� ī���� ����N(1<=N<=500,000)�� �־����� ��° �ٿ��� ���� ī�尡 �����ִ� ������ �־��� ���� ī�忡 ���� ���ڴ� -10,000,000<=L <= 10,000,000, ���� ī���� ���ڴ� ��� �ٸ�
#��° �ٿ��� M(1<=M<=500,000) , ��° �ٿ��� ����̰� ���� �ִ� ���� ī������ �ƴ��� ���ؾ� �� M���� ������ �־����� �� ���ڴ� �������� ����, �� ���ڵ� L�� ���� ����

from bisect import bisect_left, bisect_right

#N�� M�� C++�� ��쿡 �ʿ��ϱ� ������ ������ ���Ե�...
N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    #ī�尡 �����Ѵٸ�...? r-l�� 0���� ū ���ڷ� ����
    ans.append(1 if r-l else 0)

print(*ans)

#Binary Search : 