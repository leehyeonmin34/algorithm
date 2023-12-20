def solution(s):
    up_next = True
    answer = ""
    for char in s:
        answer += char.upper() if up_next else char.lower()
        up_next = True if char == " " else False
    return answer