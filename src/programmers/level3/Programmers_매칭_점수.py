

# 검색어에 대한 매칭점수를 계산
# 기본 점수 = 검색어가 등장하는 횟수(대소문자 무시)
# 외부 링크 수 = 다른 페이지로 연결된 링크 갯수
# 링크 점수 = 해당 페이지로 링크가 걸린 외부 페이지의 (기본점수 / 외부 링크 수) 총합
# 매칭점수 = 기본 점수 + 링크 점수

# 매칭점수가 가장 높은 웹페이지의 index를 구하라.
# 동일한 매칭점수를 가진 웹페이지가 여러개면 그중 index 번호가 작은 것을 리턴

# 현재 페이지 url은 <meta property="og:url" content="https://careers.kakao.com/index" />
# 외부링크는 <a href="https://careers.kakao.com/index">
# 모든 url은 https://로만 시작
# 검색어는 영소문자 1단어 (1~12자)
# 검색어와 정확히 일치하는 단어만 인정 (단어 구분은 알파벳 제외한 모든 문자로. @, 띄어쓰기, / 등)

import re, collections

def solution(word, pages):

    URL, NORMAL_SCORE, NUM_OF_LINKS, REF_TO_THIS, LINK_SCORE = range(5)
    info = [[None, 0,0,[],0] for _ in range(len(pages))]
    urls = collections.defaultdict()

    # url 찾기
    for i, page in enumerate(pages):
        url = page.split("<meta property=\"og:url\" content=\"")[1].split("\"")[0]
        info[i][URL] = url
        urls[url] = i

    for i, page in enumerate(pages):
        # 링크 찾기
        a_splits = page.split("<a href=\"")[1:]
        info[i][NUM_OF_LINKS] = len(a_splits)
        for a_split in a_splits:
            link = a_split.split("\"")[0]
            if link in urls:
                info[urls[link]][REF_TO_THIS].append(i)

        # 검색어 찾기
        info[i][NORMAL_SCORE] = re.sub("[^a-z]+", ".", page.lower()).split(".").count(word.lower())

    # 링크 점수 = 해당 페이지로 링크가 걸린 외부 페이지의 (기본점수 // 외부 링크 수) 총합
    for i in range(len(pages)):
        info[i][LINK_SCORE] = sum([ info[j][NORMAL_SCORE] / info[j][NUM_OF_LINKS] for j in info[i][REF_TO_THIS] if info[j][NUM_OF_LINKS] != 0])

    # 점수 제일 높은 페이지의 인덱스 (점수 같으면 인덱스 높은 거
    scores = [[info[i][NORMAL_SCORE] + info[i][LINK_SCORE], i] for i in range(len(pages))]
    scores.sort(key=lambda x: (x[0], x[1]))
    return scores[-1][1]

param1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
param2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution("blind", param1)) #0
print(solution("Muzi", param2)) #1