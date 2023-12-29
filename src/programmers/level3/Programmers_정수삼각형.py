def solution(triangle):
    # 1번째 줄로 초기화
    answer = triangle[0][0]

    # i 번째 줄
    for i in range(1, len(triangle)):
        prev_row = triangle[i - 1]
        curr_row = triangle[i]

        curr_row[0] += prev_row[0]
        curr_row[i] += prev_row[i - 1]
        for j in range(1, i):
            curr_row[j] += max(prev_row[j - 1], prev_row[j])
    return max(triangle[-1])