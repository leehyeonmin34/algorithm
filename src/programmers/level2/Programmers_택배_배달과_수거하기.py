import collections


def solution(cap, n, deliveries, pickups):
    def get_sliced_points(a):

        a = [0] + a
        p = []

        # 맨 우측 배달장소 p에 추가
        last = 0
        for i in range(n, -1, -1):
            if a[i]:
                p.append(i)
                last = i
                break

        c = 0
        for i in range(last, -1, -1):

            # 0인 부분은 건너 뛰기
            if a[i] == 0:
                continue

            # c가 채워지고도 남으면 그 자리에서 다시 시작할 것이니까 피봇 포인트 하나 추가
            # 딱 맞거나 모자라면 다음 택배지점에서 total > c + a[i]해져서 p에 추가될 것
            total = c + a[i]
            k = total // cap if total % cap != 0 else total // cap - 1
            p += [i] * k
            c = total - k * cap

        return p

    ds = get_sliced_points(deliveries)
    ps = get_sliced_points(pickups)

    # print(ds)
    # print(ps)

    cost = 0
    mlen = max(len(ds), len(ps))
    ds = ds + [0] * (mlen - len(ds))
    ps = ps + [0] * (mlen - len(ps))
    for i in range(mlen):
        cost += max(ds[i], ps[i])

    return cost * 2


print(solution(4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0])) # 16
print(solution(2,	7,	[1, 0, 2, 0, 1, 0, 2],	[0, 2, 0, 1, 0, 2, 0])) # 30