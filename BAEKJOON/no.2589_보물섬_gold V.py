from collections import deque
import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline

H,W = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(H)]

dr = [-1,0,0,1]
dc = [0,-1,1,0]

def bfs(r,c):
    visited = [[False]*W for _ in range(H)]
    queue = deque()
    queue.append((r,c,0))
    visited[r][c]=True

    while queue:
        r,c,cnt = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and graph[nr][nc]=="L":
                queue.append((nr,nc,cnt+1))
                visited[nr][nc] = True

    return cnt

res = 0
for r in range(H):
    for c in range(W):
        if graph[r][c]=="L":
            res = max(res, bfs(r,c)) 

print(res)

"""
https://www.acmicpc.net/problem/2589
'그래프에서 지점과 지점의 최단거리'를 구해야함
=> 시작점이 주어지지 않기 때문에 다익스트라는 아님
=> 모든 지점마다 시작해서 다른 지점까지의 최단거리를 구하는 플로이드 마샬?
=> 그래프의 방향성이나 이동거리 간의 비용차이 등이 나오지 않기 때문에
  그래프 최단거리 보다는 완전 탐색으로 생각해보기.
=> 최소거리를 구할 때 보통 사용되는 BFS로 풀자.
"""