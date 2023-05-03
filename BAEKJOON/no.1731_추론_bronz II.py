import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

a1 = arr[0]
a2 = arr[1]
aN = arr[N-1]

if (a2-a1)*(N-1)==(aN-a1):
    print(int(aN + a2-a1))
elif (a2/a1)**(N-1)==aN/a1:
    print(int(aN*(a2/a1)))
else:
    print("띠용")

