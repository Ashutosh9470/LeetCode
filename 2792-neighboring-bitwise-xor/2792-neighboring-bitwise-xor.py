class Solution:
    def doesValidArrayExist(self, derived):
        return reduce(lambda x, y: x ^ y, derived, 0) == 0