# 도넛 모양, 막대 모양, 8자 모양 그래프가 여러개 있는데
# 외부 정점 한개를 이 그래프들의 임의의 점에 연결해버림
# [외부 정점 번호, 도넛, 막대, 8자]

import collections

def solution(edges):

    outmap = collections.defaultdict(list)
    inmap = collections.defaultdict(list)
    for u, v in edges:
        outmap[u].append(v)
        inmap[v].append(u)

    line = donut = eight = start = 0

    donut_nodes = []
    line_nodes = []
    eight_nodes = []

    # 외부 정점은 out간선이 2개 이상이면서 in간선이 없음
    for node in outmap.keys():
        if len(outmap[node]) >= 2 and len(inmap[node]) == 0:
            start = node
            break

    # graph_connection_nodes = [key for key in inmap.keys() if len(inmap[key]) == 2 and len(outmap[key]) < 2]
    graph_connection_nodes = [node for node in outmap[start]]

    visit = collections.defaultdict(bool)

    for node in graph_connection_nodes:

        # 해당 점으로 들어오는 in간선이 3개라면 8자일 수밖에 없음
        if len(inmap[node]) == 3:
            eight += 1
            eight_nodes.append(node)
            continue

        # 해당 점을 시작으로 탐색 시작
        s = [node]
        while s:
            curr = s.pop()

            # 여기 방문한 적있는데 시작점과 같다면 donut으로 판단
            # 방문한적 있다면 더이상의 탐색 그만둠
            if visit[curr]:
                if curr == node:
                    donut += 1
                    donut_nodes.append(curr)
                break

            # 방문 마킹
            visit[curr] = True

            # in간선이 2개고 out간선도 2개라면 8자 그래프의 교차점이라고 간주
            if len(inmap[curr]) == 2 and len(outmap[curr]) == 2:
                eight += 1
                eight_nodes.append(node)
                break

            # 다음지점들을 스택에 추가함
            else:
                for next in outmap[curr]:
                    s.append(next)

    # 외부 정점에서 시작하는데 도착점이 도넛이나 8자가 아닌 점
    line += len([node for node in outmap[start] if node not in donut_nodes and node not in eight_nodes])

    return [start, donut, line, eight]


param1 = [[2,3],[4,3],[1,1],[2,1]]
print(solution(param1)) # [2,1,1,0]

param2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(param2)) # [4, 0, 1, 2]