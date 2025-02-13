class Solution:
    def minOperations(self, a: List[int], k: int) -> int:
        a.sort()
        b = []
        i = j = count = 0
        
        while True:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                x = a[i]
                i += 1
            else:
                x = b[j]
                j += 1
            
            if x >= k:
                return count
            
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                y = a[i]
                i += 1
            else:
                y = b[j]
                j += 1
            
            b.append(2 * x + y)
            count += 1
        return -1