class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq=defaultdict(int)
        ans, cnt, l=0, 0, 0
        for r,x in enumerate(nums):
            cnt+=freq[x]
            freq[x]+=1
            while cnt>=k:
                ans+=n-r
                freq[nums[l]]-=1
                cnt-=freq[nums[l]]
                l+=1
        return ans

               