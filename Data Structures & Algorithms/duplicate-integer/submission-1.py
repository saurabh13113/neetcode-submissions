class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        des = []
        for num in nums:
            if num not in des:
                des.append(num)
            elif num in des:
                return True
        return False
         