class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(val: int) -> int:
            chakra = str(val) 
            n = len(chakra) - len(s)  

            if n < 0:
                return 0  

            dp = [[0] * 2 for _ in range(n + 1)]

            dp[n][0] = 1
            dp[n][1] = int(chakra[n:] >= s)

            
            for i in range(n - 1, -1, -1):
                digit = int(chakra[i])

                dp[i][0] = (limit + 1) * dp[i + 1][0]

                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]

        return count(finish) - count(start - 1)