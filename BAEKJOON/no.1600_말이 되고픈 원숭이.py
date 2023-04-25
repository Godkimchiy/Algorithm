from collections import deque
import sys

sys.stdin = open("input.txt","r")

K = int(input())
W,H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

dr = [-1,0,0,1]
dc = [0,-1,1,0]
hr = [-2,-2,-1,-1,1,1,2,2]
hc = [-1,1,-2,2,-2,2,-1,1]

def bfs(sr,sc, K):
    queue = deque([])
    queue.append((sr,sc,K)) # strart r,c , coin, cnt
    cnt = [[[0]*(K+1) for _ in range(W)] for _ in range(H)] 
    
    while queue:
        r, c, coin = queue.popleft()
        # print(f"to ({r},{c}): move {cnt} times")
        if r==H-1 and c==W-1:
            return cnt[r][c][coin]
        
        if coin>0:
            for i in range(8):
                nr = r+hr[i]
                nc = c+hc[i]
                if 0<=nr<H and 0<=nc<W and graph[nr][nc]==0 and cnt[nr][nc][coin-1]==0:
                    cnt[nr][nc][coin-1] = cnt[r][c][coin]+1
                    queue.append((nr,nc,coin-1))
       
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            
            if 0<=nr<H and 0<=nc<W and graph[nr][nc]==0 and cnt[nr][nc][coin]==0:
                cnt[nr][nc][coin] = cnt[r][c][coin]+1
                queue.append((nr,nc,coin))
                
    return -1

print(bfs(0,0,K))