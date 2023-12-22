import collections


class Node:

    def __init__(self):
        self.children = collections.defaultdict()
        self.is_word = False


def solution(words):
    root = Node(None)
    for word in words:
        node = root
        for char in word:
            if char in node.children:
                next = node.children[char]
            else:
                next = Node()
                node.children[char] = next
            node = next
        node.is_word = True

    # 탐색방법 1
    # dfs방식으로 load == 1인 지점, is_word인 부분만 m을 추가시킴
    # O(M * N) 단어길이 M, 단어갯수 N
    sum = 0
    s = [[root, 0]]
    while s:
        node, m = s.pop()
        if len(node.children) == 1:
            sum += m
            continue

        sum += m if node.is_word else 0

        for key, next in node.children.items():
            s.append([next, m + 1])

    return sum

# 탐색방법 2
# 모든 단어를 root에서부터 검사해내려나감
# O(M * N) 단어길이 M, 단어갯수 N
#     total = 0
#     for word in words:
#         node = root
#         m = 0
#         for char in word:
#             node = node.children[char]
#             m += 1
#             if node.load == 1 or m == len(word):
#                 total += m
#                 break

#     return total

# 1번 방식이 더 적은 노드를 탐색해서 성능이 좋아질 줄 알았으나,
# 두 탐색 방법의 성능이 거의 차이나지 않음



def solution(words):
    answer = 0
    words.sort()
    for idx, word in enumerate(words):
        res = 1

        if idx > 0:
            for i, char in enumerate(word):
                res = max(res, i+1)
                # 이전 단어가 현재 경로와 같은 길이이거나(이전단어가 여기서 끝났을 때), 이전단어의 현재위치와는 다를 때(트라이가 분기할 때) break
                if len(words[idx-1]) == i or words[idx-1][i] != char: break
        if idx+1 < len(words):
            for i, char in enumerate(word):
                res = max(res, i+1)
                # 다음 단어가 현재 경로와 같은 길이이거나, 다음단어의 현재위치와는 다를 때(트라이가 분기할 때) break
                if len(words[idx+1]) == i or words[idx+1][i] != char: break
        answer += res

    return answer