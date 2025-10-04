class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        A, l, r=0, 0, n-1
        while l<r:
            A=max(A, min(h[l], h[r])*(r-l))
            if h[r]<h[l]: r-=1
            else: l+=1
        return A
        