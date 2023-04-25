from collections import deque
import sys

sys.stdin = open("input.txt","r")
# N  = int(sys.stdin.readline())
N  = int(input())
graph =  [list(map(int,input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
clusters = list()
dr = [-1,0,0,1]
dc = [0,-1,1,0]

def bfs(r,c):
    global cluster
    queue = deque([(r,c)])
    visited[r][c]=True
    cluster+=1
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and graph[nr][nc]==1:
                visited[nr][nc]=True
                cluster+=1
                queue.append((nr,nc))

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==1:
            cluster = 0
            bfs(i,j)
            clusters.append(cluster)

print(len(clusters))
for v in sorted(clusters):
    print(v)





    