# A가 주사위의 반을 먼저 가져감.
# A가 승리할 확률이 가장 높아지기 위해 A가 골라야할 주사위 번호를 오름차순으로 배열에 담아 반환
import collections
import itertools
from bisect import bisect_left
def solution(dice):
    answer = []

    def get_dice_permu(dices: list[list]):
        map = [0] * 501
        idxs = range(6)
        for product in itertools.product(idxs, repeat=len(dices)):
            value = 0
            i = 0
            for idx in product:
                value += dices[i][idx]
                i += 1
            map[value] += 1
        return map

    def get_win(a:list, b:list):
        rang = range(501)
        win = 0

        mapb_presum = [0] * 501
        for i in range(1, 501):
            mapb_presum[i] = mapb_presum[i - 1] + mapb[i]

        for num in range(501):
            if a[num] == 0:
                continue
            win += mapb_presum[num - 1]
        return win


    dice_idx_lst = range(len(dice))
    max_win = 0
    answer = []
    for comb in itertools.combinations(dice_idx_lst, len(dice) // 2):
        mapa = get_dice_permu([dice[i] for i in comb])
        mapb = get_dice_permu([dice[i] for i in dice_idx_lst if i not in comb])

        win_val = get_win(mapa, mapb)
        print(comb, win_val)
        if win_val > max_win:
            max_win = win_val
            answer = [i + 1 for i in sorted(list(comb))]

    return answer


# print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])) # [1]
print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])) #[1,3]