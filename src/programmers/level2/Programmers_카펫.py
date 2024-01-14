def solution(brown, yellow):
    m = brown + yellow
    s = (brown + 4) // 2

    # x가 가질 수 있는 최대값
    x_max = (s // 2)

    x = x_max // 2 # x는 x가 가질 수 있는 최대값의 절반에서 출발함
    y = s - x  # y는 x값에 따라 자동적으로 정해짐
    diff = x_max // 2 # diff는 x 출발점을 기준으로 x에 더해질 수 있고 빼질 수도 있는데, x가 x_max의 반값이니 최대 x_max 반값만큼만 커질 수 있음

    # x * y == m인 지점을 찾아나감
    while x * y != m:
        if diff != 1:
            diff //= 2

        if x * y > m:
            x -= diff
            y += diff

        else:
            x += diff
            y -= diff

    return [y, x]