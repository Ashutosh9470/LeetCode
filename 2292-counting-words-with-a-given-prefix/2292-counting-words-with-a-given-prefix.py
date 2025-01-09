class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        x=0
        for i in words:
            if i.startswith(pref):
                x += 1
        return x