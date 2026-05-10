class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for x in range(len(nums)):
            seen[nums[x]] = x

        
        for x in range(len(nums)):
            total = target - nums[x]
            if total in seen and seen[total] != x:
                return [x,seen[total]]
        return []
        