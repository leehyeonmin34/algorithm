# 1-n 번호의 사람이 영어 끝말잇기 중 (1번부터 순환 순서)
# 단어 재등장 불가. 1글자 미인정
# return [제일 먼저 탈락하는 사람의 번호, 그 사람이 자신의 몇 번째 차례에 탈락하는지]
# 탈락자 없다면 [0,0]

def solution(n, words):
    words.append(words[-1][-1] +"*"+ words[0][0])
    s = set()
    for i, word in enumerate(words):
        if word in s or words[i - 1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        s.add(word)
    return [0, 0]