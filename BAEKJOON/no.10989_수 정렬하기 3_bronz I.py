import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

cnts = [0]*10001

for _ in range(N):
    cnts[int(input())]+=1

for num, cnt in enumerate(cnts):
    if cnt>0:
        for _ in range(cnt):
            print(num)


"""
입력받는걸 저장하지 않고 바로 처리해도 괜찮다면
그렇게 하는게 메모리를 아낄 수 있음.

"""