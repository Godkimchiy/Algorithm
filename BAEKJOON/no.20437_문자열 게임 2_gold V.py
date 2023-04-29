from collections import defaultdict
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())
strings = [(str(input().rstrip()), int(input().rstrip())) for _ in range(T)]

def string_game(string, K):
    alphabets = defaultdict(list)
    for i,alphabet in enumerate(string):
        if string.count(alphabet)>=K:
            alphabets[alphabet].append(i)
    
    if not alphabets:
        return -1,
    
    len_min = 10001
    len_max = 0
    for indices in alphabets.values():
        for i in range(len(indices)-(K-1)):
            string_len = indices[i+(K-1)] - indices[i] + 1
            len_min = min(len_min, string_len)
            len_max = max(len_max, string_len)

    return len_min, len_max

for string, K in strings:
    print(*string_game(string, K))

"""
문자열은 특별한 알고리즘이 없는 느낌이다.
이번 문제에서는 생각보다 주어진 문자열 전체를 탐색하면서
알파벳 단위로 개수를 세고 길이를 계산하는 방법을 
있는 그대로 단순하게 진행했다.

배운점.
1) 문자열.count(문자) 함수
2) from collections import defaultdict
3) 두 값의 출력을 *로 곧바로 공백을 사이에 두고 출력하는게 편하고, 그러기 위해서는
  모든 리턴값이 iterable 하게 콤마를 사용해줘야 한다는 것. 

"""


    