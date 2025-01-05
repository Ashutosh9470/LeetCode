class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        output = []

        for i in reversed(nums2):
            while stack:
                if stack[-1] > i:
                    hashmap[i] = stack[-1]
                    stack.append(i)
                    break
                else: 
                    stack.pop()
            if not stack:
                hashmap[i] = -1
                stack.append(i)
        
        for j in nums1:
            output.append(hashmap[j])
        return output

        