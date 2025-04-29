class Solution(object):
    def countSubarrays(self, nums, k, left=0):
        maxi = max(nums)
        maxiOccurence = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == maxi:
                maxiOccurence += 1
            while maxiOccurence >= k:
                if nums[left] == maxi:
                    maxiOccurence -= 1
                left += 1
            res += left
        return res