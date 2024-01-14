import time
# dp
# O(N^4)
# 최악 테스트케이스 약 10초
def solution1(n):
    m = [set() for _ in range(n + 1)]
    m[1].add("()")
    answer = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            for l in m[j]:
                for r in m[i - j]:
                    m[i].add(l + r)
            for e in m[i - 1]:
                m[i].add("(" + e + ")")
    return len(m[-1])

# O(2^N)
# 최악 테스트케이스 약 4초
def solution2(n):
    answer = 0
    s = [[0, 0]]
    while s:
        l, r = s.pop()

        if l < r or l > n:
            continue

        if r == n:
            answer += 1
            continue

        s.append([l + 1, r])
        s.append([l, r + 1])

    return answer

#   n \ solution   1      2
#   14           10.8s   6.9s
#   15           43.4s   25.3s
#   16          181.1s   91.6s

# for n in range(14, 30):
#     a, b = solution1(n), solution2(n)
#     print(a, b)
#     if a < b:
#         print("end")
#         break