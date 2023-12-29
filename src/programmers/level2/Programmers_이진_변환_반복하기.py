def solution(s):
    zero, converted = 0, 0
    while s != "1":
        one = s.count("1")
        zero += len(s) - one
        converted += 1
        s = bin(one)[2:]
    return [converted, zero]


print(solution("110010101001"))