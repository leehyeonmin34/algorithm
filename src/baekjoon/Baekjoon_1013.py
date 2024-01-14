import sys, re


# (100+1+ | 01)+
class Solution():

    def solution(self, code):
        result = re.fullmatch("((100+1+)|(01))+", code)
        return "YES" if result else "NO"


# NO NO YES
solution = Solution()
for _ in range(int(sys.stdin.readline())):
    print(solution.solution(sys.stdin.readline()))

p1 = "10010111"
p2 = "011000100110001"
p3 = "0110001011001"

# solution = Solution()
# print(solution.solution(p1)) # NO
# print(solution.solution(p2)) # NO
# print(solution.solution(p3)) # YES