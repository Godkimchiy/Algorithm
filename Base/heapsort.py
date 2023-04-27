import heapq
# 기본적으로 최소 힙으로 구현되어 있음. => 작은 것부터 꺼내지기 때문에 오름차순으로 정렬할 수 있음.
def heapsort(iterable):
    h = []
    
    for v in iterable:
        heapq.heappush(h,v) # 오름차순 정렬시 사용.
        heapq.heappush(h,-v)# 내림차순 정렬시 사용.
    print(h) # 힙에 추가할 때는 정렬되지 않는다.

    result = [-heapq.heappop(h) for _ in range(len(h))] # 오름차순 정렬시 사용.
    # result = [-heapq.heappop(h) for _ in range(len(h))] # 내림차순 정렬시 사용.
    # 힙에서 빼면서 정렬이 완성됨.
    return result

ans = heapsort([1,3,5,7,9,2,4,6,8,0])
print(ans)