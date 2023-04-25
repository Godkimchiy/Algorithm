from collections import deque
import sys

sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = sys.maxsize

def dfs(start_city, curr_city, total_cost, visited):
    global res

    if len(visited)==N-1:
        res = min(res, total_cost+W[curr_city][start_city])
        return


    for city in range(N):
        if W[curr_city][city]>0 and city not in visited:
            visited.append(city)
            dfs(start_city, city, total_cost+W[curr_city][city], visited)
            visited.pop()


    return 0


for s_city in range(N):
    tot_cost = 0
    visited = list()
    dfs(s_city,s_city,tot_cost,visited)

print(res)

    
    
    
