def solution(n):
    start, end, curr = 1, 1, 1
    answer = 1  # 자기 자신 1개인 경우를 이미 포함

    # 연속된 숫자영역의 왼쪽 오른쪽에 포인터를 두고 이동
    # 첫 수가 n의 절반보다 작을 때까지만 계산
    while start <= n // 2:
        if curr >= n:
            if curr == n:
                answer += 1
            curr -= start
            start += 1
        else:
            end += 1
            curr += end

    return answer