class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:

        ctr, ans = defaultdict(int), 0

        for x, y in dominoes:
            ctr[1<<x | 1<<y]+= 1
        
        for cnt in ctr.values():
            ans+= cnt * (cnt - 1)

        return ans//2 