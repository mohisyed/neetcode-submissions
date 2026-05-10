class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for num in range(len(nums)):
            counter = 0
            for sub in range(num+1,len(nums)):
                if nums[num] + nums[sub] == target:
                    return [num,sub]