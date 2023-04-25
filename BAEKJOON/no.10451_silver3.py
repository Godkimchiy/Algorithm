from collections import deque
import sys

sys.stdin = open("input.txt","r")
N_test = int(sys.stdin.readline())
test_cases = list()
for _ in range(N_test):
    N_node = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    test_cases.append((N_node, arr))


def dfs(start_node, curr_node):
    visited[curr_node]=True
    next_node = arr[curr_node]-1
    if not visited[next_node]:
        dfs(start_node, next_node)


for N_node, arr in test_cases:
    cnt=0
    visited = [False]*N_node

    for s_node in range(N_node):
        if not visited[s_node]:
            next_node = arr[s_node]-1
            dfs(s_node, next_node)
            cnt+=1

    print(cnt)