class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dq = deque([(0, 0)])
        dist[0][0] = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        
        while dq:
            x, y = dq.popleft()
            curDir = grid[x][y] - 1
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if 0 <= nx < m and 0 <= ny < n:
                    cost = dist[x][y] + (0 if dir == curDir else 1)
                    if cost < dist[nx][ny]:
                        dist[nx][ny] = cost
                        if dir == curDir:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        
        return dist[m - 1][n - 1]