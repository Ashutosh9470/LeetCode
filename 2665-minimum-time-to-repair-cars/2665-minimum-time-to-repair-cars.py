import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n=len(ranks)
        def possible_contribution(max_time):
            count_cars=0
            for i in range(n):            
                count_cars+= int(math.sqrt(max_time//ranks[i]))
            return True if count_cars>=cars else False

        l=1
        r=cars*cars*100
        ans=r
        while l<=r:
            mid=(r-l)//2 + l
            if possible_contribution(mid):
                ans = mid
                r=mid-1
            else:
                l=mid+1
        return ans