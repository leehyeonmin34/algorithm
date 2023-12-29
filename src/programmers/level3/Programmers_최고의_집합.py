def solution(n, s):
    if n > s: return [-1]
    share, remain = divmod(s, n)
    return [share] * (n  - remain) + [share + 1] * remain