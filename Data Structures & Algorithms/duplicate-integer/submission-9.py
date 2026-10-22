class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
            elif i in l:
                return True
        return False
        