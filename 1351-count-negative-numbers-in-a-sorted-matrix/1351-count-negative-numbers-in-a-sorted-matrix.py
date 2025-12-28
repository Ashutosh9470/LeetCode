class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=0
        for i in grid:
            for j in i:
                if j <0:
                    x=x+1
        return x