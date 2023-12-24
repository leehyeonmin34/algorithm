import heapq

def solution(operations):

    min_q, max_q = [], []
    min_out, max_out = [], [] # 각각, min, max q에서 나갔어야 하는 숫자들

    # 명령어 수행
    for op in operations:
        if op[0] == "I": # 큐에 넣기
            val = int(op[2:])
            heapq.heappush(min_q, val)
            heapq.heappush(max_q, -val)
            # if val in min_out:
                # min_out.remove(val)
            # if val in max_out:
                # max_out.remove(val)

        elif op[2] == "1": # 최댓값 "D 1 XX"
            while max_q:
                val = -heapq.heappop(max_q)
                if val in max_out:
                    max_out.remove(val)
                else:
                    # print(op, "최댓값", val)
                    min_out.append(val)
                    break
        else: # 최솟값 "D -1 XX"
            while min_q:
                val = heapq.heappop(min_q)
                if val in min_out:
                    min_out.remove(val)
                else:
                    # print(op, "최솟값", val)
                    max_out.append(val)
                    break

    # 최종 최대, 최소 추출
    # print(min_q, max_q)
    max_q_result = set([-n for n in max_q])
    result = set(min_q).intersection(max_q_result)
    return [max(result), min(result)] if result else [0,0]