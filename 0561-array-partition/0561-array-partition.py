class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        sol = 0
        while nums:
            p1, p2 = nums.pop(), nums.pop()
            sol += p2
        
        return sol