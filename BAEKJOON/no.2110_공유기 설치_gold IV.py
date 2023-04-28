import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N,C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start = 1
end = houses[-1]-houses[0]
res = 0
while start<=end:
    mid = (start+end)//2

    pick = houses[0]
    cnt = 1
    for house in houses:
        if house-pick>=mid:
            cnt+=1
            pick = house
    
    if cnt < C:
        end = mid-1
        continue
    elif cnt >= C:
        start = mid+1
        res = max(res, mid)

print(res)


"""
최적의 조건을 찾아가는 문제이기 때문에 단순히 순차 탐색보다는 이진 탐색으로 진행함.
'가장 인접한 두 공유기 사이의 거리'를 최대로 하는 것이기 때문에 공유기 간의 거리를
변수로 두고 탐색해야한다. 또한 그 거리의 최솟값을 구하는 것이라는 것도 놓치지 말기.

"""



