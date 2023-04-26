import sys

sys.stdin = open("input.txt","r")

K, N = map(int, input().split())
array = [int(input()) for _ in range(K)]

s_idx = 1 # 이거 주의! 랜선의 길이니깐 1이상이어야 함. 항상 인덱스로 생각하지 말기.
e_idx = max(array)
res = 0

while s_idx<=e_idx:
    mid = (s_idx+e_idx)//2
    total = 0
    for ran in array:
        total += ran//mid
    
    if total < N:
        e_idx = mid-1
    else:
        s_idx = mid+1
        res = max(res, mid)

print(res)