class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = target
        for count1 in range(len(nums)):
            for count2 in range(len(nums)):
                if count1 != count2:
                    if target == nums[count1] + nums[count2]:
                        return [count1,count2]
                
        