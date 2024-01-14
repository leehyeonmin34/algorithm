def solution(s):
    answer = -1

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return (not stack) * 1