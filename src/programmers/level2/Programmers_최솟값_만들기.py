def solution(a, b):
    N = len(a)
    a.sort()
    b.sort(reverse=True)

    return sum([a[i] * b[i] for i in range(N)])