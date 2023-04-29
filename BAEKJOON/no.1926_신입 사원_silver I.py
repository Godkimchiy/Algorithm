import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted([list(map(int,input().split())) for _ in range(N)])
    min_v = arr[0][1]
    cnt=1
    for _,v2 in arr[1:]:
        if min_v>v2:
            cnt+=1
            min_v = v2
    print(cnt)

"""
하나를 기준으로 정렬해서 비교하려 접근했고,
다른 하나가 다른 애들에 비해 뒤지면 안된다는 말을 이해하는 데
시간이 좀 걸림;;
"""