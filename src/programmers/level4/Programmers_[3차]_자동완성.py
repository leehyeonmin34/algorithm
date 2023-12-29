import collections

# 노드를 활용해서 이것저것 시도해봤지만,
# 그래프만으로 하는 게 노드 활용하는 것보다 성능 2배 좋음
# defaultdict보다 그냥 dict가 성능 살-짝 더 좋은 것 같기도 함
def solution(words):

    # 각 노드가 딕셔너리로서 표현되며,
    # 해당 노드의 일반 자식은 char key를 갖고,
    # 속성값은 DUP, END 같은 별도의 key를 갖는다.
    DUP, END = "DUP", "END"

    # 트라이 그래프 생성
    root = {}
    for word in words:
        curr = root
        for char in word:
            curr = curr.setdefault(char, {})
            curr[DUP] = 1 if DUP not in curr else curr[DUP] + 1

        curr[END] = True

    # dfs로 가지쳐지는 부분이나 단어가 끝나는 부분 탐색
    sum = 0
    s = [[root, 0]]
    while s:
        curr, m = s.pop()

        # 중복이 1인 곳(더 이상 탐색 필요 X)
        if DUP in curr and curr[DUP] == 1:
            sum += m
            continue

        # 단어가 끝나는 부분
        sum += m if END in curr else 0

        # 자식 노드들 추가
        for key, next in curr.items():
            if key not in [DUP, END]:
                s.append([next, m + 1])

    return sum


# 노드 활용
# class Node:
#
#     def __init__(self):
#         self.children = collections.defaultdict()
#         self.is_word = False
#
# def solution(words):
#     root = Node()
#     for word in words:
#         node = root
#         for char in word:
#             if char in node.children:
#                 next = node.children[char]
#             else:
#                 next = Node()
#                 node.children[char] = next
#             node = next
#         node.is_word = True

    # # 노드 활용 탐색방법 1
    # # dfs방식으로 load == 1인 지점, is_word인 부분만 m을 추가시킴
    # # O(M * N) 단어길이 M, 단어갯수 N
    # sum = 0
    # s = [[root, 0]]
    # while s:
    #     node, m = s.pop()
    #     if len(node.children) == 1:
    #         sum += m
    #         continue
    #
    #     sum += m if node.is_word else 0
    #
    #     for key, next in node.children.items():
    #         s.append([next, m + 1])
    #
    # return sum

# 노드 활용 탐색방법 2
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


# 노드 활용 탐색방법 3
# Node를 사용해 children의 갯수를 이용해 비교
# 1,2번과 성능 비슷함

# def solution(words):
#     root = Node()
#     for word in words:
#         node = root
#         for char in word:
#             if char in node.children:
#                 next = node.children[char]
#             else:
#                 next = Node()
#                 node.children[char] = next
#             node = next
#         # node.children["end"] = Node()
#         node.is_word = True
#
#     sum = 0
#     for word in words:
#         children = root.children
#         duplicated_pos = 0
#         for i, letter in enumerate(word):
#             curr = children[letter]
#
#             # 자식이 여러개이거나 자식이 하나지만 여기가 단어의 마지막인 마지막 지점을 다음 인덱스를 duplicated_pos로 지정
#             if len(curr.children) > 1 or curr.is_word and len(curr.children) > 0:
#                 duplicated_pos = i + 1 # i는 letter의 인덱스, i + 1는 children의 인덱스
#
#             children = curr.children
#
#         if duplicated_pos == 0:
#             sum += 1
#             print(word, 1)
#         elif duplicated_pos < len(word):
#             sum += duplicated_pos + 1
#             print(word, duplicated_pos + 1)
#         elif duplicated_pos == len(word):
#             sum += duplicated_pos
#             print(word, duplicated_pos)
#
#     return sum



print(solution(["word","war","warrior","world"])) # 15