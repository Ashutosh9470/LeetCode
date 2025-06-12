class Solution:
    def __init__(self):
        self.pre = []

    # even or odd
    def parity(self, num):
        return num & 1

    def max_subarray_sum(self, a, b, s, k):
        n = len(s)
        l, r = 0, k - 1

        r_freq_a = r_freq_b = 0
        l_freq_a = l_freq_b = 0

        sum_val = float('-inf')
        # mat denotes second part, we have to minimize it
        INF = int(1e8)
        mat = [[INF, INF], [INF, INF]]

        while r < n:
            # update right-side prefix counts
            r_freq_a = self.pre[a][r + 1]
            r_freq_b = self.pre[b][r + 1]

            # can we move window from left
            while r - l + 1 >= k and (r_freq_b - l_freq_b) >= 2:
                # update current minimum
                mat[self.parity(l_freq_a)][self.parity(l_freq_b)] = min(
                    mat[self.parity(l_freq_a)][self.parity(l_freq_b)],
                    l_freq_a - l_freq_b
                )

                # move towards next window
                l_freq_a = self.pre[a][l + 1]
                l_freq_b = self.pre[b][l + 1]
                l += 1

            # calculate current subarray sum
            calc = (r_freq_a - r_freq_b) - mat[self.parity(r_freq_a) ^ 1][self.parity(r_freq_b)]
            sum_val = max(sum_val, calc)
            r += 1

        return sum_val

    def maxDifference(self, s, k):
        n = len(s)
        # resizing the vector to n+1 length and 5 size i.e. 0,1,2,3,4
        self.pre = [[0] * (n + 1) for _ in range(5)]

        for i in range(n):
            # move all frequencies to current index
            for j in range(5):
                self.pre[j][i + 1] = self.pre[j][i]
            conv = int(s[i])
            self.pre[conv][i + 1] += 1

        diff = float('-inf')

        # going from all possible pairs
        for i in range(5):
            if self.pre[i][n] == 0:
                continue
            for j in range(5):
                if i == j or self.pre[j][n] == 0:
                    continue
                calc = self.max_subarray_sum(i, j, s, k)
                diff = max(diff, calc)

        return int(diff)