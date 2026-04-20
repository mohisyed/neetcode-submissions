class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for z in range(len(nums)):
            numsOfZ = 0
            for x in range(len(nums)):
                if nums[z] == nums[x]:
                    if numsOfZ < 1:
                        numsOfZ += 1
                    else:
                        return True 

        return False
        