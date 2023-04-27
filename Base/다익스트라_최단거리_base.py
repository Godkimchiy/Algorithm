# 본 코드는 간단한 구현 방법
# 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다.
# 따라서, 전체 시간 복잡도는 O(V^2)이다.
# 일반적으로, 노드 개수가 5,000개 이하로 주어지는 경우 이렇게 해결 가능하다.
# 하지만 10,000개 이상이 될 경우, 다른 방법이 필요하다.
# 이를 위해 우선순위 큐(Priority Queue)를 사용함.

import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = sys.maxsize
# 노드 개수, 간선 개수
N, M = map(int, input().split())
print(N,M)
# 출발 노드
start = int(input())
# 경로 및 비용(거리) 그래프
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s_node, e_node, distance = map(int,input().split())
    graph[s_node].append((e_node, distance))
# 방문 정보
visited = [False]*(N+1)
# 최단거리 테이블
shortest = [INF]*(N+1)

# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
def new_start_node():
    min_distance = INF
    new_node = -1
    for node in range(1,N+1):
        if not visited[node] and shortest[node]<min_distance:
            min_distance=shortest[node]
            new_node = node
    return new_node

# 다익스트라 알고리즘
def dijkstra(start):
    # 1. 시작 노드 설정
    shortest[start] = 0 #
    visited[start] = True
    # 2. 시작 노드를 거치는 경로들에 대해 최단거리 테이블 갱신.
    for e_node,distance in graph[start]:
        shortest[e_node] = distance
    while sum(visited)<N: # 모든 노드들을 방문할 때 까지 반복.
        curr_node = new_start_node()
        visited[curr_node]=True
        for e_node,distance in graph[curr_node]:
            shortest[e_node] = min(shortest[e_node], shortest[curr_node]+distance)
            # 이렇게 min을 하는게 빠를까 조건을 거는게 빠를까?

dijkstra(start)

# 출발 노드부터 다른 모든 노드들까지의 최단 거리.
for node in range(1,N+1):
    if shortest[node]==INF:
        print("inf")
    else:
        print("To. node",node,":",shortest[node])


