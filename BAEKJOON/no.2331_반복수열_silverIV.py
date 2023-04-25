import sys

sys.stdin = open("input.txt","r")
A,P = map(int, sys.stdin.readline().split())

D = [A]

while True:
    v = D[-1]
    v_list = list(map(int, list(str(v))))
    
    new_v = sum([v**P for v in v_list])

    if new_v in D:
        dup_v_idx = D.index(new_v)
        break
    D.append(new_v)
    
print(len(D[:dup_v_idx]))