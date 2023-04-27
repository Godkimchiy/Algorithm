"""조합(combinations) nCr 구현!

1. itertools 사용하기
- itertools.combinations(list,r)

2. DFS 사용하기
- 깊이가 r을 초과하지 않도록
"""

X = ['a', 'b', 'c', 'd', 'e', 'f']

# 방법 1.
# import itertools
# r = 2
# res = list(map(list, itertools.combinations(X,r)))

# 방법 2.
n = len(X)
r = 2
res = []

def dfs(idx, list):
    if len(list)==r:
        res.append(list[:])
        return
    
    for i in range(idx,n):
        dfs(i+1, list+[X[i]])

dfs(0,[])
print(res)