import sys
sys.stdin = open("input.txt","r")

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

mino = [(3,0),(0,3),(1,1)]
excld = [
    [(0,0),(0,2)], [(1,0),(1,2)], [(1,0),(0,2)], [(0,0),(1,2)],
    [(0,1),(0,2)], [(1,1),(1,2)], [(0,0),(0,1)], [(1,0),(1,1)],
]

def all_case(sr,sc):
    ans = 0
    for dr,dc in mino:
        er = sr+dr
        ec = sc+dc
        if 0<=er<N and 0<=ec<M:
            region=[graph[r][c] for r in range(sr,er+1) for c in range(sc,ec+1)]
            ans = max(ans, sum(region))

    er = sr+2
    ec = sc+3
    if 0<=er<N and 0<=ec<M:
        for conds in excld:
            region=[graph[sr+i][sc+j] for i in range(2) for j in range(3) if (i,j) not in conds]
            ans = max(ans, sum(region))
    
    er = sr+3
    ec = sc+2
    if 0<=er<N and 0<=ec<M:
        for conds in excld:
            region=[graph[sr+i][sc+j] for i in range(3) for j in range(2) if (i,j) not in [(c,r) for (r,c) in conds]]
            ans = max(ans, sum(region))
    
    return ans
            
res=0
for i in range(N):
    for j in range(M):
        res = max(res, all_case(i,j))

print(res)
