import sys
sys.stdin = open("input.txt","r")

N=int(input())
arr=[int(input()) for _ in range(N)]

dp=[0]*(N)
if len(arr)<=2:
    print(sum(arr))
else:
    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    for i in range(2,N):
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(dp[-1])


"""
i-th 점수를 무조건 사용하는 것이 중요함 => 연속 세 번 불가 조건을 제어할 수 있음.
연속 세 번 불가 조건
=> i-3, i-2 까지의 최대값을 기준으로 계산함.
=> 그 이후에 i-1, i를 어떻게 사용해서 i-th까지 최대를 만들지
  조건을 고려해서 점화식을 만듦.
"""