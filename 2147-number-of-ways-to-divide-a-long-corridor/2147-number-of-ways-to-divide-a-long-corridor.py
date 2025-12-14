class Solution(object):
    def numberOfWays(self, corridor):
        mod = 10**9 + 7
        pos = []

        for i, c in enumerate(corridor):
            if c == 'S':
                pos.append(i)

        if len(pos) % 2 == 1 or len(pos) == 0:
            return 0

        res = 1
        for i in range(2, len(pos), 2):
            len_of_gap = pos[i] - pos[i - 1]
            res = (res * len_of_gap) % mod

        return res