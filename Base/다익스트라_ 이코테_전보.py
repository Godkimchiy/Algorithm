import heapq
import sys
sys.stdin = open("input.txt","r")
INF = sys.maxsize
input = sys.stdin.readline

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

# 최소비용 테이블
timer = [INF]*(N+1)

def dijkstra(start):
    timer[start] = 0
    hq = []
    heapq.heappush(hq,(0, start))

    while hq:
        time_sum, curr_city = heapq.heappop(hq)

        if timer[curr_city]<time_sum:
            continue

        for e_city, time in graph[curr_city]:
            if time_sum+time < timer[e_city]:
                timer[e_city] = time_sum+time
                heapq.heappush(hq, (time_sum+time, e_city))

dijkstra(C)

city_cnt = 0
max_time = 0
for city in range(1,N+1):
    if timer[city]!=INF:
        city_cnt += 1
        max_time = max(max_time,timer[city])
print(f"{city_cnt-1} {max_time}")
# print(timer)


