def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        elif stack and stack[-1] == "(":
            stack.pop()
        else:
            return False

    return True if not stack else False