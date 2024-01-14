# k칸 앞으로 점프 : k 
# (현재까지 거리 * 2) 위치로 순간이동 : 0
# 순간이동이 좋음
# return N으로 가는데 필요한 최소 건전지 사용량

def solution(n):
    jump = 0
    while n > 0:
        jump += n % 2
        n >>= 1
    return jump