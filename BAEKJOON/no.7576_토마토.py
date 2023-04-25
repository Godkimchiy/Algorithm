from collections import deque
import sys

sys.stdin = open("input.txt","r")

M,N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1,0,0,1]
dc = [0,-1,1,0]

def bfs(tomato_states):
    queue = deque()
    start = []
    for r in range(N):
        for c in range(M):
            if graph[r][c]==1:
                start.append((r,c))
    queue.append(start)
    
    if len(queue)==0:
        return -1, tomato_states

    cnt=0

    while queue:
        day_q = queue.popleft()
        next_q = list()
        change=0
        for r,c, in day_q: # 이게 다 빠져야 하루 카운트
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0<=nr<N and 0<=nc<M and tomato_states[nr][nc]==0:
                    tomato_states[nr][nc]=1
                    change+=1
                    next_q.append((nr,nc))
                    
        if change>0:
            cnt+=1
            queue.append(next_q)

    return cnt,tomato_states


days,graph = bfs(graph)
for row in graph:
    if 0 in row:
        days=-1
        break

print(days)


"""
<내가 생각했던 포인트>
- 최소일수(=최소이동수)를 구할 때는 BFS 사용.
- 이웃들이 모두 Q에서 빠져야 일수 카운트.
- 시작 점이 여러 개일 수 있다. => 입력을 받고 1을 세지 말고, 시작점을 Q에 넣을 때 탐색하기.

<다른 사람 코드>
- 리스트의 pop은 O(n), Q의 popleft는 O(1).
- 내가 이웃들이 모두 빠져야 일수를 카운트하게 한걸 간단하게 만들 수 있다
- 그래프 상에서 익는걸 1로만 할 필요없이 맨처음 익어있는 토마토부터 시작해서 1씩
  더해주면서 카운트하면된다.
"""
#