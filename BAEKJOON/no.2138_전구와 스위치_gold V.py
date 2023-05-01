import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
state = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))
res = 100001
def solution(state, cnt):
    global res
    temp = state[:]
    touch = 0
    touch += cnt
    for i in range(1,N):
        if temp[i-1]==goal[i-1]:
            continue
        cnt+=1
        for j in range(3):
            ni = i-1+j
            if 0<=ni<N:
                temp[ni] = 1-temp[ni]
    
    if temp==goal:
        res = min(res,cnt)

solution(state,0)

state[0]=1-state[0]
state[1]=1-state[1]
solution(state,1)

if res==100001:
    print(-1)
else:
    print(res)