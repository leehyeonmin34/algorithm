import itertools
import copy, heapq


def solution(board, r, c):
    BOARD_SIZE = 4
    CHARACTERS_AND_EMPTY = 6 + 1
    UP, DOWN, LEFT, RIGHT = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    X, Y = 0, 1
    directions = [UP, DOWN, LEFT, RIGHT]

    def in_board(x, y):
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    # src -> dst의 최단경로 비용을 리턴함
    def move(board, src, dst):
        visited = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        enqueued = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        q = [[0, *src]]
        while q:
            cost, a, b = heapq.heappop(q)

            if visited[a][b]:
                continue
            visited[a][b] = 1

            if [a, b] == dst:
                return cost

            # 각 방향에 대해
            for dir in directions:

                # 한 칸 이동
                x, y = a + dir[X], b + dir[Y]
                if in_board(x, y) and not visited[x][y] and not enqueued[x][y]:
                    heapq.heappush(q, [cost + 1, x, y])
                    enqueued[x][y] = 1

                # Ctrl 이동. 보드바깥으로 나가거나 캐릭터 마주칠때까지
                while in_board(x, y) and not board[x][y]:
                    x += dir[X]
                    y += dir[Y]
                if not in_board(x, y):  # 보드 밖으로 나갔으면 다시 안으로 들임
                    x -= dir[X]
                    y -= dir[Y]
                if not visited[x][y] and not enqueued[x][y]:
                    heapq.heappush(q, [cost + 1, x, y])
                    enqueued[x][y] = 1

    def no_card_left(unopened):
        for char_cards in unopened:
            if char_cards:
                return False
        return True

    # 각 캐릭터별 카드위치들을 넣을 map
    # cards[character] = location_list
    unopened = [[] for _ in range(CHARACTERS_AND_EMPTY)]
    enter = 0
    for i, j in itertools.product(range(BOARD_SIZE), repeat=2):
        char = board[i][j]
        if char:
            unopened[char].append([i, j])
            enter += 1

    print(unopened)
    print(list(itertools.permutations(filter(lambda v: v, [cards for cards in unopened]))))

    # 캐릭터들을 회수하는 최소비용을 다익스트라로 구함
    q = [[0, unopened, board, [r, c]]]
    while q:
        cost, unopened, board, curr = heapq.heappop(q)

        # 모두 다 찾았으면 끝
        if no_card_left(unopened):
            return cost + enter

        for character, char_cards in enumerate(unopened):

            # 해당 캐릭터카드 찾을 필요 없으면 다음으로
            if not char_cards:
                continue

            card1, card2 = char_cards

            # curr -> 1 -> 2, curr -> 2 -> 1 경로 비용 계산
            cost1 = move(board, curr, card1) + move(board, card1, card2)
            cost2 = move(board, curr, card2) + move(board, card2, card1)

            # card1, card2 뒤집기
            n_board = copy.deepcopy(board)
            n_board[card1[X]][card1[Y]] = 0
            n_board[card2[X]][card2[Y]] = 0
            n_unopened = copy.deepcopy(unopened)
            n_unopened[character] = []

            # 힙에 추가. 최소비용이 더 크더라도 종료시 커서 위치가 다르기 때문에 둘 다 추가함.
            heapq.heappush(q, [cost + cost1, n_unopened, n_board, card2])
            heapq.heappush(q, [cost + cost2, n_unopened, n_board, card1])

# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0)) #14
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],	0,	1)) #16