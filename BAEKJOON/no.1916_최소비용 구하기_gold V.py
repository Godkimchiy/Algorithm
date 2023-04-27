import heapq
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s_city, e_city, cost = map(int, input().split())
    graph[s_city].append((e_city, cost))
start_city, destination = map(int, input().split())

min_cost = [INF]*(N+1)

def dijkstra(start):
    min_cost[start]=0
    hq=[]
    heapq.heappush(hq,(0,start))

    while hq:
        cost_sum, curr_city = heapq.heappop(hq)
        
        if min_cost[curr_city] < cost_sum:
            continue

        for e_city, cost in graph[curr_city]:
            if cost_sum+cost < min_cost[e_city]:
                min_cost[e_city]=cost_sum+cost
                heapq.heappush(hq, (cost_sum+cost, e_city))

dijkstra(start_city)
print(min_cost[destination])

"""
N개의 노드.
노드 간의 방향성이 있고 음이 아닌 비용.
한 지점에서 다른 지점까지의 최소 비용.
=> 다익스트라

다익스트라 함수 정의하고, 수행하는 코드 빼먹지 말기..!
"""