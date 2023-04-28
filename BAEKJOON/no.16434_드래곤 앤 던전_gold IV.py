import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = sys.maxsize

N, ATK = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

start = 1
end = INF

def adventure(HP_max):
    HP_cur = HP_max
    H_atk = ATK
    print(f"출발. HPcur:{HP_cur}  |ATK:{H_atk}")
    for i in range(N):
        t,a,h = info[i]
        if t==2:
            print(f"\nstage.{i+1} '포션' ATK:+{a}, HP:+{h}")
            H_atk+=a
            HP_cur = min(HP_max, HP_cur+h)
            print(f"상태: HPcur:{HP_cur}  |ATK:{H_atk}")
        else:
            print(f"\nstage.{i+1} '몬스터' ATK:{a}, HP:{h}")
            ntimes = h//H_atk if h%H_atk==0 else h//H_atk+1
            print(f"{ntimes}번 싸움진행")
            h -= H_atk*ntimes
            HP_cur -= a*(ntimes)
            if h <= 0:
                HP_cur += a
                print(f"이김: HPcur:{HP_cur}  |ATK:{H_atk} |몬스터HP:{h}")
            
            if HP_cur<=0:
                print(f"패배: HPcur:{HP_cur}  |ATK:{H_atk} |몬스터HP:{h}")
                return False
    return True
    

res = 0
while start<=end:
    print(f"\n탐색범위:{start}~{end}")
    mid = int((start+end)//2)
    if adventure(mid):
        end = mid -1
        res = mid
    else:
        start = mid+1

print(res)

"""
내 접근: HP max를 변수로 잡고 최소값을 구해야하니 HP_max의 상한을 찾자
내가 놓친 부분1: 접근까지는 좋았지만 어디서 상한을 얻을 수 있을지 알지 못함.
개선 방안: 문제에서 '최악의 상황'이 무엇일지 생각해보자.
         여기서는 모든 방에 몬스터가 있고, 모든 방에서 몬스터들의 공격을 받는 것.
         이러기 위해서는 atk는 최소, a는 최대여야 한다.
내가 놓친 부분2: binary search 함수를 최적의 값을 찾는 과정 중간에 사용하는 방법도 있다는것!
내가 놓친 부분3: 상한값을 maxsize를 사용할 수 있다.
내가 놓친 부분4: 몬스터랑 싸우는 턴을 반복문이 아니라 횟수를 세야 시간초과가 나지 않음.
"""
