import collections
import heapq


def solution(begin, target, words):
    def get_path_len(path):
        path.pop(begin)
        curr = target
        result = 0
        while True:
            prev, curr = curr, path[curr]
            if curr:
                result += 1
            else:
                return result

    map = collections.defaultdict(list)

    words.append(begin)
    for word in words:
        for i in range(len(word)):
            start, end = word[:i], word[i + 1:]
            for alphabet in "abcdefghijklmnopqrstuvwxyz":
                new_word = start + alphabet + end
                if new_word in words and new_word not in map[word] and new_word != word:
                    map[word].append(new_word)

    dist = collections.defaultdict(str)
    for key in words:
        if key == begin:
            dist[key] = 0
        else:
            dist[key] = 9999999

    q = [(0, begin)]
    path = collections.defaultdict(str)

    while q:
        u = heapq.heappop(q)[1]
        for v in map[u]:
            if dist[u] < dist[v] + 1:  # 기존 경로보다 v를 들렀다 u로가는게 더 빠르면 v가 새 최적경로
                dist[u] = dist[v] + 1
                path[u] = v
            heapq.heappush(q, (dist[v], v))
        if u == target:
            return get_path_len(path)
        map[u] = []
    return 0