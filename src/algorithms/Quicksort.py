def quicksort(array):
    def bfs(left, right):
        if left >= right:
            return

        # 가운데 원소를 피봇으로 선정
        pivot_idx = left + (right - left) // 2
        pivot = array[pivot_idx]

        # 피봇보다 작은건 피봇 왼쪽에,큰 건 오른쪽에
        # 왼쪽에서부터 i가 피봇보다 큰 거, 오른쪽에서부터 j가 피봇보다 작은 걸 찾아내서
        # 둘이 swap한다
        i, j = left, right
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        # 내부적으로
        bfs(left, i - 1)
        bfs(i, right)

    bfs(0, len(array) - 1)
    return array


print(quicksort([5,3,6,4,8,5,3,2,9,1]))