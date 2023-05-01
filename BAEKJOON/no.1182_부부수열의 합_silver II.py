import sys
from itertools import combinations

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for l in range(1,N+1):
    cases = combinations(arr, l)
    for case in cases:
        if sum(case)==S:
            cnt+=1

print(cnt)