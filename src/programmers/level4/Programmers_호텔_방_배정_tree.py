# 신청한 순서대로 방을 배정
# 요청한 방에 먼저 배정. 없다면 더 번호가 큰 방 중 제일 번호가 작은 방

class PointerNode:
    def __init__(self, val):
        self.val = val
        self.next: PointerNode = None
        self.load = 0


class RoomNode:

    def __init__(self, num):
        self.occupied = False
        self.pointer: PointerNode = None
        self.num = num


def solution(k, room_number):
    def get_root(room: RoomNode):
        pointer = room.pointer
        while pointer.next:
            pointer = pointer.next
        return pointer

    answer = []

    rooms = []
    for i in range(k + 1):
        room = RoomNode(i)
        pointer = PointerNode(i)
        pointer.load = 1
        room.pointer = pointer
        rooms.append(room)

    for n in room_number:

        # 점유된 노드일때 pointer를 따라 점유되지 않은 노드로 이동
        curr = rooms[n]
        if curr.occupied:
            root_room_num = get_root(curr).val
            curr = rooms[root_room_num]

        # 점유처리
        answer.append(curr.num)
        curr.occupied = True

        # 점유 후 포인터 수정
        prev = rooms[curr.num - 1]
        next = rooms[curr.num + 1] if curr.num + 1 <= k else None

        if not next:
            continue

        ## 앞뒤로 점유되었다면, 좌우의 root 병합
        if prev.occupied and next.occupied:
            next_root = get_root(next)
            curr_root = get_root(curr)
            load_sum = curr_root.load + next_root.load
            # if curr_root.load > next_root.load:
            if True:
                next_root.next = curr_root
                curr_root.val = next_root.val
                curr_root.load = load_sum
            else:
                curr_root.next = next_root
                next_root.load = load_sum


        ## prev만 점유되었을 때. curr root를 우측으로 확장하고, next가 이걸 참조하게 함.
        elif prev.occupied:
            curr_root = get_root(curr)
            curr_root.val = next.num
            next.pointer = curr_root
            curr_root.load += 1

        ## prev가 점유되지 않았을 때. next는 점유되든 말든.
        ## next_root를 좌측으로 확장(curr이 next_root에 편입함)
        elif not prev.occupied:
            next_root = get_root(next)
            curr.pointer = next_root
            next_root.load += 1

    return answer