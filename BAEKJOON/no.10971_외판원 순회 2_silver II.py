import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = int(1e7)

def dfs(start, curr, cost, cnt):
    global ans
    
    if cnt==N:
        if graph[curr][start]>0:
            cost += graph[curr][start]
            ans = min(ans, cost)
        return
    
    if cost>ans: # 도달하지 못 했는데 이미 비용이 초과하면 그만 가기.
        return
    
    for e_city, fee in enumerate(graph[curr]):
        if fee>0 and not visited[e_city]:
            visited[e_city]=True
            dfs(start, e_city, cost+fee, cnt+1)
            visited[e_city]=False

for s_city in range(N):
    visited = [False]*N
    visited[s_city]=True
    dfs(s_city, s_city, 0, 1)

print(ans)


"""
dfs + 조건을 사용한 백트래킹 문제.
모든 경우를 살피며 조건으로 가지치기.

포인트.
- 시작점을 방문처리 및 카운트하고 시작한다는 점.

"""