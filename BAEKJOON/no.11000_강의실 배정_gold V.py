import sys
import heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _  in range(N)])
class_room_q = list()
heapq.heappush(class_room_q,schedules[0][1])

for i in range(1,N):
    if class_room_q[0]<=schedules[i][0]:
        heapq.heappop(class_room_q)
    heapq.heappush(class_room_q, schedules[i][1])

print(len(class_room_q))

"""
동시간대에 존재했던 강의의 최대 수를 구하면 됨.
강의 마다 겹치는지를 확인하기 위해 heapq를 사용한다는 점.
확인하는 강의의 시작 시간 이하인 강의 종료 시간들이 큐에 여러개 있어도,
그 중 하나만 빼는 이유는 현재 확인 중인 강의는 하나니깐 같이 쓸 강의실 하나만 있어도 된다.
"""