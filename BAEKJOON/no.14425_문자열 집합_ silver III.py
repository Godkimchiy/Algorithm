import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input().rstrip())

cnt = 0
for _ in range(M):
    if input().rstrip() in S:
        cnt+=1

print(cnt)