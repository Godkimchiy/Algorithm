import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
d = [0]*(k+1)

for coin in coins:
    for won in range(coin,k+1):
        if won==coin:
            d[won]+=1
        d[won] += d[won-coin]
    
print(d[k])


"""
각 coin마다 해당 코인을 1개만 사용해주는 경우 1을 더해준다.
이걸 두 번째 반복문 시작전에 더해줬더니 에러가 났음.
왤까...?
"""