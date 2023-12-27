import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    for _ in range(n):
        x = -heapq.heappop(heap)
        heapq.heappush(heap, 1 - x)
    return sum([work ** 2 for work in heap])

p11, p12 = 4, [4, 3, 3]	#12
p21, p22, = 1, [2, 1, 2]	#6
p31, p32 = 3, [1,1]	#0

print(solution(p11, p12)) #12
print(solution(p21, p22)) #6
print(solution(p31, p32)) #0