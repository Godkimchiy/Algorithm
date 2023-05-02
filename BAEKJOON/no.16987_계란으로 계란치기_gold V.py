import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def break_egg(pick):
    global ans
    if pick==N:
        cnt = 0
        for i in range(N):
            if eggs[i][0]<=0:
                cnt+=1
        ans = max(ans,cnt)
        
        return
    
    if eggs[pick][0]<=0:
        break_egg(pick+1)
        return
    
    unbroken = 1
    for i in range(N):
        if i!=pick and eggs[i][0]>0:
            unbroken+=1
    if unbroken==1:
        ans = max(ans, N-1)
        return

    for i in range(N):
        if i==pick:
            continue
        
        if eggs[i][0]<=0:
            continue

        eggs[i][0] -= eggs[pick][1]
        eggs[pick][0] -= eggs[i][1]

        break_egg(pick+1)

        eggs[i][0] += eggs[pick][1]
        eggs[pick][0] += eggs[i][1]

break_egg(0)
print(ans)

"""
그리디.
종료 조건이 많았던 느낌.
진행 중인데 깰 수 있는 애들이 없었던 케이스를 놓쳤었음.
"""
