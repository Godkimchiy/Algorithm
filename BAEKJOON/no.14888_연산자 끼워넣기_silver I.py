import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split())) # +, -, x, %

res_max = -sys.maxsize
res_min = sys.maxsize

def dfs(idx, cum_value, plus,minus,multiply,divide):
    global res_max, res_min

    if idx==N:
        res_max = max(res_max,cum_value)
        res_min = min(res_min,cum_value)

    if plus: # +
        dfs(idx+1, cum_value+arr[idx], plus-1,minus,multiply,divide)
    if minus: # -
        dfs(idx+1, cum_value-arr[idx], plus,minus-1,multiply,divide)
    if multiply: # x
        dfs(idx+1, cum_value*arr[idx], plus,minus,multiply-1,divide)
    if divide: # %
        dfs(idx+1, int(cum_value/arr[idx]), plus,minus,multiply,divide-1)

dfs(1, arr[0], *ops)

print(res_max)
print(res_min)



"""
깊이마다 개수가 변경되는건 파라미터로 두는 것.
여기서 연산자 수까지도.

최댓값을 음수로 초기화 해야할 경우도 있다!

몫만 취한다길래 // 연산자를 사용했는데, 음수를 나눠야하는 일 때문인지 /와 int를 사용해야 정답이 나온다.
ex)    -10//3 => -4
   int(-10/3) => -3
"""