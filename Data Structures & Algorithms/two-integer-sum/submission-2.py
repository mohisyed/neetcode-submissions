class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        totalDict = {}

        for x in range(len(nums)):
            totalDict[nums[x]] = x
        

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in totalDict and totalDict[diff] != i:
                return [i,totalDict[diff]]
        return []

        