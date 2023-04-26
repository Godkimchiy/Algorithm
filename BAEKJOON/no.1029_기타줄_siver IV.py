import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
six_min = 1001
one_min = 1001
for i in range(M):
    a,b = map(int, input().split())
    six_min = min(a,six_min)
    one_min = min(b,one_min)

if six_min<one_min*6:
    res = min(six_min*(N//6)+one_min*(N%6),six_min*(N//6+1))
else:
    res = one_min*N
print(res)

"""
어떤 유형의 문제일까 고민했지만, 유형을 따지지 않고, 세트이든 낱개이든 최소값만
있으면 된다고 생각함. (내가 유형을 모를지도..ㅎ)
=> 그리디 알고리즘 유형이라고 함.
그리디 알고리즘? 매 스텝마다 최적의 방향으로 결정하며 진행하는 방식.

여기서 조심해야할건 세트가 무조건 더 싸다는 조건이 없기 때문에 그렇지 않은 경우까지
고려해야함. 그리고 맨 처음 모든 가격의 정보를 갖고있을 필요는 없음.

"""
