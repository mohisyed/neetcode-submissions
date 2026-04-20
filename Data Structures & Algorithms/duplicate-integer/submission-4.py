class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums = set(nums)
        print(len(newNums))
        print(len(nums))
        if len(newNums) != len(nums):
            return True
        return False
        