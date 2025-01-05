class Solution:
    def calculateScore(self, s: str) -> int:
        seen = [[] for i in range(26)]
        res = 0
        for i, c in enumerate(s):
            a = ord(c) - ord('a')
            if seen[25 - a]:
                j = seen[25 - a].pop()
                res += i - j
            else:
                seen[a].append(i)
        return res