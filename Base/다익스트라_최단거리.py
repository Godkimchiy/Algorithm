# 우선순위 큐(Priority Queue)를 사용한 효율적인 방법.
# 최단 거리가 가장 짧은 노드를 찾는 데 O(N)이 소요되던 것을
# O(logN)으로 단축시킴.

import sys
import heapq
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
# 최단거리 테이블
shortest = [INF]*(N+1)

# 다익스트라 알고리즘
def dijkstra(start):
    # 1. 시작 노드 설정
    hq = list()
    heapq.heappush(hq, (0,start))
    shortest[start] = 0
    
    # 2. 시작 노드를 거치는 경로들에 대해 최단거리 테이블 갱신.
    while hq: # 모든 노드를 Q에 넣어 살피기 위해 Q가 비워질 때까지 수행.
        cost_sum, curr_node = heapq.heappop(hq) # 최단 거리가 가장 짧은 노드 찾기.
        
        # 현재 노드로 cost_sum의 비용으로 왔는데, 이미 더 싸게 올 수 있다면 넘어가기.
        if shortest[curr_node]<cost_sum:
            continue
        
        for e_node,cost in graph[curr_node]:
            if shortest[e_node]>cost_sum + cost:
                shortest[e_node] = cost_sum + cost
                heapq.heappush(hq,(cost_sum + cost, e_node))


dijkstra(start)

# 출발 노드부터 다른 모든 노드들까지의 최단 거리.
for node in range(1,N+1):
    if shortest[node]==INF:
        print("inf")
    else:
        print("To. node",node,":",shortest[node])


