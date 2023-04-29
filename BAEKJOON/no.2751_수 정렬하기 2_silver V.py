import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
for v in arr:
    print(v)


"""
메모리가 보장이되니 sorted 가 통하네.
sorted 가 최악의 경우에도 O(nlog n)을 보장해준다고 알고있음.
"""