import heapq


# 끝시간을 포함
# YYYY-MM-DD hh:mm:ss.sss rs

# 이 풀이는 heap을 사용하기 때문에 nlogn 소요
# 시작시간과 끝시간을 2개의 리스트로 나눠서 최저시간 기준으로 탐색하면 O(n) 가능
# float을 이용한 second 단위로 풀면 안되는데 부동소수점 문제 같다.
# int의 ms 단위로 풀어야 풀린다.
def solution(lines):
    def to_sec(t: str):
        h, m, s = map(float, t.split(":"))
        return int( 1000 * float(h * 3600 + m * 60 + s))

    def duration_to_int(t: str):
        return int(1000 * float(t[:-1]))

    START_AFTER_999, END = 0, 1

    q = []
    for line in lines:
        _date, time, duration = line.split(" ")
        end = to_sec(time)
        start = to_sec(time) - duration_to_int(duration) + 1
        heapq.heappush(q, [start - 999, START_AFTER_999])
        heapq.heappush(q, [end, END])

    cnt = 0
    m = -1
    while q:
        t, type = heapq.heappop(q)
        if type == START_AFTER_999:
            cnt += 1
            m = max(m, cnt)
        else:
            cnt -= 1

    return m


# 7
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))