import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dictionary = {}
idx = 0
for v in sorted(arr):
    if v not in dictionary.keys():
        dictionary[v]=idx
        idx+=1

res = []
for v in arr:
    res.append(dictionary[v])

print(*res)

"""
정렬 문제에서는 항상 딕셔너리 사용을 고려하자.
"""