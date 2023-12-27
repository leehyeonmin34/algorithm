# 신청한 순서대로 방을 배정
# 요청한 방에 먼저 배정. 없다면 더 번호가 큰 방 중 제일 번호가 작은 방

def solution(k, room_number):

    map = {}

    def find(n):
        visited = [n]
        while n in map and map[n] != n:
            n = map[n]
            visited.append(n)
        map[n] = n
        for i in visited:
            map[i] = n

        return n

    answer = []

    for n in room_number:
        root = find(n)
        answer.append(root)
        map[root] = find(root + 1)

    return answer


print(solution(10,	[1,3,4,1,3,1]))
