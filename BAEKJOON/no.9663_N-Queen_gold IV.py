import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

def possible_loc(col):
    for i in range(col):
        if rows[col]==rows[i] or abs(rows[col]-rows[i])==abs(col-i):
            return False
    return True


rows = [N]*N
cnt = 0

def dfs(col):
    global cnt

    if col==N: # 끝까지 오면 조건에 맞게 놓을 수 있어야 한다.
        cnt+=1
        return
    
    for row in range(N):
        rows[col]=row
        if possible_loc(col):
            dfs(col+1)

dfs(0)
print(cnt)
    